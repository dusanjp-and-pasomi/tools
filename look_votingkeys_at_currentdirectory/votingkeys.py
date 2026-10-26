#!/usr/bin/env python3
"""
votingkey.py
今いるディレクトリの private_key_tree*.dat の詳細を表示する
"""

import os
import re
import glob


def xxd_epoch(file_path):
    try:
        with open(file_path, "rb") as f:
            # オフセット 0x0001 と 0x0000 を読み込む（StartEpoch）
            f.seek(0x0001)
            byte1_start = f.read(1)
            f.seek(0x0000)
            byte2_start = f.read(1)

            # オフセット 0x0009 と 0x0008 を読み込む（EndEpoch）
            f.seek(0x0009)
            byte1_end = f.read(1)
            f.seek(0x0008)
            byte2_end = f.read(1)

            if not byte1_start or not byte2_start or not byte1_end or not byte2_end:
                print("Error: File is too short to read specified offsets.")
                return

            # StartEpoch: 0x0001 + 0x0000 を連結して10進数に変換
            hex_start = byte1_start.hex() + byte2_start.hex()
            dec_start = int(hex_start, 16)

            # EndEpoch: 0x0009 + 0x0008 を連結して10進数に変換
            hex_end = byte1_end.hex() + byte2_end.hex()
            dec_end = int(hex_end, 16)

            print("StartEpoch:\t" + str(dec_start))
            print("EndEpoch:\t" + str(dec_end))
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")


def xxd_like_dump(file_path, start_offset=0x0020, end_offset=0x003F):
    try:
        with open(file_path, "rb") as f:
            f.seek(start_offset)
            offset = start_offset
            hex_concatenated = ""

            while offset <= end_offset:
                chunk = f.read(min(16, end_offset - offset + 1))
                if not chunk:
                    break

                for b in chunk:
                    hex_concatenated += f"{b:02X}"

                offset += 16

            print(f"publicKey:\t{hex_concatenated}")
            xxd_epoch(file_path)
            print(f"filename:\t{os.path.basename(file_path)}")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")


def process_voting_keys():
    """今いるディレクトリの private_key_tree*.dat を処理"""
    files = glob.glob("private_key_tree*.dat")

    if not files:
        print("votingKeyはありません。")
        return

    print("votingKey情報:\t")

    def get_number(filename):
        match = re.search(r"private_key_tree(\d+)\.dat", filename)
        return int(match.group(1)) if match else 0

    # 番号の降順でソート
    sorted_files = sorted(files, key=get_number, reverse=True)

    for i, file_path in enumerate(sorted_files):
        xxd_like_dump(file_path)
        if i < len(sorted_files) - 1:
            print()


def main():
    process_voting_keys()


if __name__ == "__main__":
    main()
