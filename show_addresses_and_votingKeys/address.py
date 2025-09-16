import sys
import os
import re
import glob
import argparse
import configparser
from getpass import getpass
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from symbolchain.CryptoTypes import PrivateKey, PublicKey
from symbolchain.facade.SymbolFacade import SymbolFacade
from symbolchain.symbol.KeyPair import KeyPair

NODE_KEY_PEM = "/cert/node.key.pem"
REMOTE_KEY_PEM = "/remote.pem"
VRF_KEY_PEM = "/vrf.pem"

def xxd_epoch(file_path):
    try:
        with open(file_path, 'rb') as f:
            # オフセット0x0001と0x0000を読み込む（StartEpoch）
            f.seek(0x0001)
            byte1_start = f.read(1)
            f.seek(0x0000)
            byte2_start = f.read(1)
           
            # オフセット0x0009と0x0008を読み込む（EndEpoch）
            f.seek(0x0009)
            byte1_end = f.read(1)
            f.seek(0x0008)
            byte2_end = f.read(1)
           
            if not byte1_start or not byte2_start or not byte1_end or not byte2_end:
                print("Error: File is too short to read specified offsets.")
                return
           
            # StartEpoch: 0x0001 + 0x0000を連結して10進数に変換
            hex_start = byte1_start.hex() + byte2_start.hex()
            dec_start = int(hex_start, 16)
           
            # EndEpoch: 0x0009 + 0x0008を連結して10進数に変換
            hex_end = byte1_end.hex() + byte2_end.hex()
            dec_end = int(hex_end, 16)
           
            # StartEpochとEndEpochを2行で表示（タブで数字を揃える）
            print("StartEpoch:\t" + str(dec_start))
            print("EndEpoch:\t" + str(dec_end))
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")

def xxd_like_dump(file_path, start_offset=0x0020, end_offset=0x003f, lines_per_page=24):
    try:
        with open(file_path, 'rb') as f:
            # 開始オフセットにシーク
            f.seek(start_offset)
            offset = start_offset
            line_count = 0
            hex_concatenated = ""
            
            while offset <= end_offset:
                # 16バイトずつ、または残りのバイトを読み込む
                chunk = f.read(min(16, end_offset - offset + 1))
                if not chunk:
                    break
                
                # 16進数を大文字で連結
                for b in chunk:
                    hex_concatenated += f"{b:02X}"
                
                offset += 16
                line_count += 1
                
                # ページング処理
                if line_count % lines_per_page == 0:
                    input("Press Enter to continue...")
            
            # 連結された16進数文字列を1行で表示（タブを追加）
            print(f"publicKey:\t{hex_concatenated}")
            
            # xxd_epochを呼び出してStartEpochとEndEpochを表示
            xxd_epoch(file_path)
            
            # ファイル名を表示（タブを追加）
            print(f"filename:\t{os.path.basename(file_path)}")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")

def process_voting_keys():
    """keys/voting または node/keys/voting 内の private_key_tree*.dat ファイルを処理"""
    # 検索するディレクトリ
    voting_dirs = [
        os.path.normpath("keys/voting"),
        os.path.normpath("node/keys/voting")
    ]
    
    voting_dir = None
    for dir_path in voting_dirs:
        if os.path.exists(dir_path):
            voting_dir = dir_path
            break
    
    if not voting_dir:
        print("votingKeyはありません。")
        return
    
    # private_key_tree*.dat ファイルを取得
    files = glob.glob(os.path.join(voting_dir, "private_key_tree*.dat"))
    
    if not files:
        print("votingKeyはありません。")
        return
    
    # votingKey情報ヘッダーを表示
    print("votingKey情報:\t")
    
    # ファイル名から番号を抽出し、降順にソート
    def get_number(filename):
        match = re.search(r'private_key_tree(\d+)\.dat', filename)
        return int(match.group(1)) if match else 0
    
    sorted_files = sorted(files, key=get_number, reverse=True)
    
    # 各ファイルに対して xxd_like_dump を実行
    for i, file_path in enumerate(sorted_files):
        xxd_like_dump(file_path)
        # ファイルごとの結果を区切るために空行を追加（最後のファイルでは追加しない）
        if i < len(sorted_files) - 1:
            print()

def get_network_name(config_path):
    """コンフィグファイルからネットワーク名を取得する"""
    config = configparser.ConfigParser()
    paths_to_check = [config_path]
    
    # カレントディレクトリの一つ上の階層のshoestringディレクトリをチェック
    parent_path = os.path.normpath(os.path.join(os.path.dirname(os.getcwd()), "shoestring", "shoestring.ini"))
    paths_to_check.append(parent_path)
    
    for path in paths_to_check:
        try:
            if os.path.exists(path):
                config.read(path, encoding="utf-8")
                return config.get("network", "name", fallback="testnet")
        except Exception:
            continue
    
    print("shoestring.ini が見つかりませんでした。デフォルトの 'testnet' を使用します。")
    return "testnet"

def read_public_keys_from_pem_chain(cert_path):
    """PEMファイルから公開鍵を取得し、リストで返す"""
    paths_to_check = [cert_path]
    
    # node/keys/ ディレクトリをチェック
    if os.path.basename(cert_path) == "node.full.crt.pem":
        node_path = os.path.normpath(os.path.join("node", cert_path))
        paths_to_check.append(node_path)
    
    for path in paths_to_check:
        try:
            with open(path, "rb") as cert_file:
                pem_data = cert_file.read()
                # PEM証明書ごとに分割
                certs = pem_data.split(b"-----END CERTIFICATE-----")
                public_keys = []
                for cert_pem in certs:
                    cert_pem = cert_pem.strip()
                    if cert_pem:
                        cert_pem += b"\n-----END CERTIFICATE-----\n"
                        cert = x509.load_pem_x509_certificate(cert_pem, default_backend())
                        # 16進文字列で表示
                        der_bytes = cert.public_key().public_bytes(
                            encoding=serialization.Encoding.DER,
                            format=serialization.PublicFormat.SubjectPublicKeyInfo,
                        )
                        der_bytes = der_bytes[12:] # 先頭12バイトを削除
                        public_keys.append(der_bytes)
                return public_keys
        except Exception:
            continue
    print(f"{os.path.basename(cert_path)} が見つかりませんでした。")
    return []

def read_private_key_from_pem(pem_path):
    """PEMファイルから秘密鍵を取得し、16進文字列で返す"""
    paths_to_check = [pem_path]
    
    # node/keys/ ディレクトリをチェック（ca.key.pem以外の場合）
    if os.path.basename(pem_path) != "ca.key.pem":
        node_path = os.path.normpath(os.path.join("node", pem_path))
        paths_to_check.append(node_path)
    
    # 親ディレクトリをチェック（ca.key.pemの場合）
    if os.path.basename(pem_path) == "ca.key.pem":
        parent_path = os.path.join(os.path.dirname(pem_path), "..", "ca.key.pem")
        paths_to_check.append(os.path.normpath(parent_path))
    
    for path in paths_to_check:
        try:
            with open(path, "rb") as ca_key_file:
                ca_key_data = ca_key_file.read()
                try:
                    # まずパスワードなしで試みる
                    private_key_obj = serialization.load_pem_private_key(
                        ca_key_data, password=None, backend=default_backend()
                    )
                except (ValueError, TypeError):
                    # パスワードが必要な場合、ユーザーにパスワードを入力させる（非表示）
                    password = getpass(f"Enter password for {os.path.basename(path)}: ").encode('utf-8')
                    if not password:
                        print(f"Password not provided for {os.path.basename(path)}.")
                        continue
                    try:
                        private_key_obj = serialization.load_pem_private_key(
                            ca_key_data, password=password, backend=default_backend()
                        )
                    except Exception as e:
                        print(f"Failed to decrypt {os.path.basename(path)}: Invalid password or corrupted key.")
                        continue
                
                der_bytes = private_key_obj.private_bytes(
                    encoding=serialization.Encoding.DER,
                    format=serialization.PrivateFormat.PKCS8,
                    encryption_algorithm=serialization.NoEncryption(),
                )
                der_bytes = der_bytes[16:] # 先頭16バイトを削除
                return der_bytes.hex().upper()
        except FileNotFoundError:
            continue
    print(f"{os.path.basename(pem_path)} が見つかりませんでした。")
    return None

def show_account_info(args, facade, account_type, private_key_path, cert_index, label):
    """アカウント情報を表示する共通関数"""
    # 秘密鍵を読み込む
    private_key_hex = read_private_key_from_pem(private_key_path)
    if private_key_hex is not None:
        key_pair = KeyPair(PrivateKey(private_key_hex))
        private_public_key = key_pair.public_key
    else:
        private_public_key = None
    
    # 証明書から公開鍵を取得（main/nodeのみ）
    cert_public_key = None
    cert_public_account = None
    if account_type in ("main", "node"):
        cert_public_keys = read_public_keys_from_pem_chain(
            args.keys_path + "/cert/node.full.crt.pem"
        )
        if not cert_public_keys or len(cert_public_keys) <= cert_index:
            print(f"証明書から{label}公開鍵の取得に失敗しました。")
            return
        cert_public_key = PublicKey(cert_public_keys[cert_index])
        cert_public_account = facade.create_public_account(cert_public_key)
        # 秘密鍵と証明書の公開鍵が一致するかチェック
        if private_public_key is not None and private_public_key != cert_public_key:
            print(f"{label}証明書の秘密鍵と公開鍵が一致しません。")
            return
    
    # アカウント情報を表示（タブを追加）
    print(f"{label}アカウント情報:\t")
    if cert_public_account:
        print(f"アドレス:\t{cert_public_account.address}")
        print(f"公開鍵:\t\t{cert_public_key}")
    elif private_public_key is not None:
        # remote/vrfは証明書がないので秘密鍵から生成
        account = facade.create_public_account(private_public_key)
        print(f"アドレス:\t{account.address}")
        print(f"公開鍵:\t\t{private_public_key}")
    else:
        print(f"{label}キーの秘密鍵が読み込めませんでした。")
        return
    if args.show_private_key and private_key_hex is not None:
        print(f"秘密鍵:\t\t{private_key_hex}")
    print() # 空行を追加して見やすくする

def show_all_keys(args):
    """メイン、ノード、リモート、VRFアカウント情報を全て表示する"""
    facade = SymbolFacade(get_network_name(args.config))
    show_account_info(args, facade, "main", args.ca_key_path, 1, "メイン")
    show_account_info(args, facade, "node", args.keys_path + NODE_KEY_PEM, 0, "ノード")
    show_account_info(args, facade, "remote", args.keys_path + REMOTE_KEY_PEM, None, "リモート")
    show_account_info(args, facade, "vrf", args.keys_path + VRF_KEY_PEM, None, "VRF")

def get_common_showkey_args():
    """共通の引数を定義するヘルパー関数"""
    parent = argparse.ArgumentParser(add_help=False)
    parent.add_argument(
        "-c",
        "--config",
        type=str,
        default="shoestring/shoestring.ini",
        help="ノードコンフィグパス[default: shoestring/shoestring.ini]",
    )
    parent.add_argument(
        "-ca",
        "--ca-key-path",
        type=str,
        default="ca.key.pem",
        help="CA証明書パス[default: ca.key.pem]",
    )
    parent.add_argument(
        "-k",
        "--keys-path",
        type=str,
        default="keys",
        help="keysディレクトリパス[default: keys]",
    )
    parent.add_argument(
        "-p",
        "--show-private-key",
        action="store_true",
        help="プライベートキーを表示する",
    )
    return parent

def get_common_link_args():
    """共通の引数を定義するヘルパー関数"""
    parent = argparse.ArgumentParser(add_help=False)
    parent.add_argument(
        "-c",
        "--config",
        type=str,
        default="shoestring/shoestring.ini",
        help="ノードコンフィグパス[default: shoestring/shoestring.ini]",
    )
    parent.add_argument(
        "-k",
        "--keys-path",
        type=str,
        default="keys",
        help="keysディレクトリパス[default: keys]",
    )
    return parent

def link_node_keys(args):
    print("ノードキーをリンクする機能はまだ実装されていません。")

def unlink_node_keys(args):
    print("ノードキーをアンリンクする機能はまだ実装されていません。")

def main():
    parser = argparse.ArgumentParser(description="エージェントS")
    subparsers = parser.add_subparsers(
        title="サブコマンド", metavar="", dest="command"
    )
    
    # サブコマンド: show-key
    show_common_args = [get_common_showkey_args()]
    show_parser = subparsers.add_parser(
        "show-key", help="すべてのノードキー情報を表示", parents=show_common_args
    )
    show_parser.set_defaults(func=show_all_keys)
    
    # サブコマンド: link
    link_common_args = [get_common_link_args()]
    link_parser = subparsers.add_parser(
        "link", help="ハーベスティングリンク", parents=link_common_args
    )
    link_parser.set_defaults(func=link_node_keys)
    
    # サブコマンド: unlink
    unlink_parser = subparsers.add_parser(
        "unlink", help="ハーベスティングアンリンク", parents=link_common_args
    )
    unlink_parser.set_defaults(func=unlink_node_keys)
    
    # 引数が指定されていない場合、デフォルトで show-key -p を実行
    if len(sys.argv) == 1:
        # デフォルト引数を設定
        args = parser.parse_args(["show-key", "-p"])
        args.func(args)
        print() # サブコマンドと投票キーの出力を分離
        process_voting_keys()
    else:
        # 引数が指定された場合は通常の処理
        args = parser.parse_args()
        args.func(args)
        print() # サブコマンドと投票キーの出力を分離
        process_voting_keys()

if __name__ == "__main__":
    main()
