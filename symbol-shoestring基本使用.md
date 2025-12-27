作業環境は  
2025_08 時点にて 
contabo vpsシリーズ  
ubuntu22/24  
で動作を確認しています。  
  
# symbol-shoestringとは

symbol-shoestringとは、symbol networkを構成する nodeを作成する為の  
ツールです。  
これの他に、symbol-bootstrapがありますが、  
こちらは、2025年に公式のサポートの終了が発表されています。  
※2025年 9月に bootstrapの新 ver.は発表されました。
現在、公式が正式にサポートしているものは、symbol-shoestringとなります。  
以下は、symbol-shoestring(2025_09_05の時点では、バージョンは 0.2.1になります。)  
を使用した、symbol-shoestringの導入と、これを使用した symbol nodeの作成手順です。  
サーバを借りてからの手順となります。
  
# 【①　nodeを作成、操作する為のユーザの作成】

* ユーザを作成し、パスワードを設定する。  
adduser [ユーザ名]  
  
* ユーザが sudoを使える様にする。  
gpasswd -a [ユーザ名] sudo  
  
* sshで接続する際の条件を変更する為に設定ファイル内容を編集、変更する。  
vi /etc/ssh/sshd_config  
  
変更内容：  
sshで接続する際に使用する portを変更する。  
#Port22　→　Port [変更したい port番号]  
  
rootとしてsshでの接続を禁止  
PermitRootLogin yes　→　PermitRootLogin no  
  
変更を保存して viを終了する。  
  
* 設定を反映させる為に sshdを再起動する。  
systemctl restart sshd  
  
--------------------------  
## ※以下は ubuntu24での 追加の接続 portの変更となります。  
* /etc/ssh/sshd_config.d/99-override.confを作成、編集する。  
vi /etc/ssh/sshd_config.d/99-override.conf  
記述内容：  
Port [変更したい port番号]  
  
* /usr/lib/systemd/system/ssh.socketを編集する。
vi /usr/lib/systemd/system/ssh.socket  
変更内容：  
ListenStream=22　→　ListenStream=[変更したい port番号]  
  
* 設定を反映させる為に daemonと sshを再起動する。  
systemctl daemon-reload  
systemctl restart ssh  
  
  
* 確認  
ss -anlt  
Local Address:Portに[変更した port番号]があるか？  
  
	systemctl status ssh.socket  
	Listen: に[変更した port番号]があるか？  
  
--------------------------  
  
* 端末を閉じずに新しく端末を開き、変更した設定でログイン出来るかを確認する。  
ssh -p [設定した port] [ユーザ名]@[サーバの IP]  
ログイン出来た場合は、最初に開いた端末を閉じて良い。  
ログイン出来なかった場合は、最初に開いた端末で、  
設定をやり直して、再度設定した内容でログイン出来るか試す。  
  
  
以降は設定変更した後にログインした端末から作業をする。  
  
# 【②　nodeを動作させる為の docker、docker-composeの導入】
  
* dockerの導入  
sudo curl https://get.docker.com | sh  
  
* ユーザを dockerグループに追加する。  
sudo usermod -aG docker $USER  
  
* dockerを起動する。  
sudo systemctl start docker  
  
* システム起動時に自動的に dockerを開始する様に設定する。  
sudo systemctl enable docker  
  
* dockerがインストールされたかを、バージョン表示で確認する。  
docker -v  
  
  
* docker-composeの導入  
  
※最新のバージョンの確認先  
https://github.com/docker/compose/releases  
  
最新のバージョンの docker-composeを導入する。  
VERSION=$(curl --silent https://api.github.com/repos/docker/compose/releases/latest | grep -Po '"tag_name": "\K.*\d')  
sudo curl -L "https://github.com/docker/compose/releases/download/${VERSION}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose  
  
※バージョンを指定してインストールする場合（v2.29.2の場合）  
sudo curl -L https://github.com/docker/compose/releases/download/v2.29.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose  
v2.29.2の部分を変更してインストールしたいバージョンを変更する。  
  
* ユーザが docker-composeを使用出来る様にする。  
sudo chmod +x /usr/local/bin/docker-compose  
  
* docker-composeがインストールされたかを、バージョン表示で確認する。  
docker-compose -V  
  
  
* dockerを再起動する。  
sudo systemctl restart docker  
  
* ユーザを dockerグループに追加した設定を反映させる為に、一旦ログアウトして再ログインする。  
sudo su  
su [ユーザ名]  
  
* ユーザが dockerグループに入っているかを確認する。  
docker ps  
ユーザが dockerグループに入っていれば、エラーは出ない。  
  
# 【③　symbol-shoestringをインストールする（venvを使用した方法）】
  
* symbol-shoestringに必要なライブラリをインストールする。  
sudo apt-get install -y libssl-dev  
sudo apt install -y build-essential python3-dev  
※これらが無いとsymbol-shoestringのインストールの途中でエラーが出る。  
  
* pythonの仮想環境を作成する venvを導入する。  
version=$(python3 -V | sed 's/^P/p/; s/ //g' | sed 's/\.[^\.]*$//')  
sudo apt install -y $version-venv  
※$versionの部分は OSのバージョンによって異なる。  
  
* venvを使用して python仮想環境 envを$HOMEに作成する。  
python3 -m venv ~/env  
※envの部分は任意で変更可能。  
  
* 作成した python仮想環境 envに入る。  
source ~/env/bin/activate  
※仮想環境から出る場合は、deactivate  
  
* symbol-shoestringをインストールする。  
pip install symbol-shoestring  
※バージョン指定する場合は、例：0.1.3　pip install symbol-shoestring==0.1.3  
  
* symbol-shoestringがインストールされたかを確認する。  
python3 -m shoestring  
※コマンドの説明が表示されたら成功。  
  
# 【④　nodeを作成する】
  
* 必要なファイル  
1.	ca.key.pem	（mainAccountの秘密鍵を保存している。）　　
2.	shoestring.ini	（nodeの基本設定。個別設定である roles、https使用の可否、CAの設定も含む。）  
3.	overrides.ini	（nodeの個別の設定）  
(4).	rest_overrides.json  
※restに変更を付与する時に必要。これが無くても nodeは作成出来る。  
  
  
* nodeを作成する作業ディレクトリを作成する。（ここでは symbolnodeとする）  
mkdir symbolnode  
  
* 作業ディレクトリに入る  
cd symbolnode  
  
----
* 1.ca.key.pemを作成する。  
mainaccountを作成する。  
python3 -m shoestring pemtool --output ca.key.pem --ask-pass  
秘密鍵を聞かれるので、秘密鍵を入力する。ca.key.pemが作成される。  
  
引数の説明：  
--output		出力先。ca.key.pemでも ca.keyでも ca.key.pemが作成される。abcなら abc.pemとなる。  
--ask-pass		パスワードを掛ける  
--input		秘密鍵を記述したファイルを指定する。  
--force		同名のファイルが既にあっても上書きする。  
  
新規で作成したい時は  
openssl genpkey -algorithm ed25519 -out ca.key.pem  
  
新規で暗号化して作成したい時は  
openssl genpkey -algorithm ed25519 -out ca  
openssl pkey -in ca -out ca.key.pem -aes256  
rm -f ca  
  
----
* 2.shoestring.iniを作成する。  
node設定ファイルを収納する shoestringディレクトリを作成する。  
mkdir shoestring  
  
node設定ファイル shoestring.iniを shoestringディレクトリ内に作成する。  
python3 -m shoestring init shoestring/shoestring.ini  
※testnetの場合は、この後に --package saiを付ける。  
  
shoestring.iniを編集する。  
vi shoestring/shoestring.ini  
  
```
[node]
caCommonName = CA [nodeの名称等]
nodeCommonName = [nodeの名称等]
```
  
ーーdualnodeーー  
```
[node]
features = API | HARVESTER
lightApi = false
```
  
ーーpeernode(lightApiを使用)ーー  
```
[node]
features = API | HARVESTER
lightApi = true
```
  
ーーpeernode(lightApiを使用しない)ーー  
```
[node]
features = HARVESTER
lightApi = false
```
  
shoestring.iniの各項目の説明  
```
 	features = API | HARVESTER | VOTER	※ﾉｰﾄﾞの種類を選んで変更する
	API			apinode
	HARVESTER	peernode
	VOTER		votingnode

	apiHttps = false				※httpsを使うか？ trueか falseにする
	lightApi = false				※lightApiを使用するか？ trueか falseにする
```
  
----
* 3.overrides.iniを作成する。  
node設定ファイル overrides.iniを shoestringディレクトリ内に作成する。  
vi shoestring/overrides.ini  
  
ーー以下をコピーしてペーストするーー  
```
[user.account]
enableDelegatedHarvestersAutoDetection = true

[harvesting.harvesting]
maxUnlockedAccounts = 5
beneficiaryAddress =

[node.node]
minFeeMultiplier = 100

[node.localnode]
host =
friendlyName =
```
ーー以上をコピーしてペーストするーー  
  
編集する項目  
```
maxUnlockedAccounts		最大委任者数
beneficiaryAddress		委任者報酬の25%を受け取るアドレス
minFeeMultiplier		最小手数料設定
host					IPまたはドメイン
friendlyName			nodeに付与する名称
```
  
ーー以下は編集後の例ーー  
```
[user.account]
enableDelegatedHarvestersAutoDetection = true

[harvesting.harvesting]
maxUnlockedAccounts = 50
beneficiaryAddress = xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

[node.node]
minFeeMultiplier = 10

[node.localnode]
host = myNodeHost
friendlyName = myNodeName
```
ーー以上は編集後の例ーー  
  
* symbol-bootstrapで作成した nodeから、transport/remote/vrf（votingnodeの場合は、votingKeyも）を インポートする際の命令  
python3 -m shoestring import-bootstrap --config shoestring/shoestring.ini --bootstrap [bootstrapで建てた nodeの targetのパス] --include-node-key  
  
----
* nodeをセットアップする。  
python3 -m shoestring setup --ca-key-path ca.key.pem --config shoestring/shoestring.ini --overrides shoestring/overrides.ini --directory $(pwd)  
※testnetの場合は、この後に --package saiを付ける。  
※別に作成した rest_overrides.jsonを反映させる場合は、--rest-overrides [rest_overrides.jsonのパス]を付ける。  
  
# 【⑤　nodeの 操作及び動作確認】
  
以下は作業ディレクトリから命令を実行する。  
  
* 1.開始  
docker-compose up -d  
  
* 2.停止  
docker-compose down  
  
* 3.動作確認  
python3 -m shoestring health --config shoestring/shoestring.ini --directory $(pwd)  
  
* 4.blockdataをリセット  
python3 -m shoestring reset-data --config shoestring/shoestring.ini --directory $(pwd)  
  
* 5.node証明書の更新  
python3 -m shoestring renew-certificates --config shoestring/shoestring.ini --ca-key-path ca.key.pem --directory $(pwd) --retain-node-key  
  
* 6.node証明書の期限の確認  
openssl x509 -noout -dates -in keys/cert/node.crt.pem  
  
* 7.異常停止等で blockdataが破損した時の処理  
docker compose -f docker-compose-recovery.yaml up --abort-on-container-exit  
  
* 8.設定変更した shoestring.ini、overrides.iniを反映させる  
python3 -m shoestring upgrade --config shoestring/shoestring.ini --overrides shoestring/overrides.ini --directory $(pwd)  
※testnetの場合は、この後に --package saiを付ける。  
※別に作成した rest_overrides.jsonを反映させる場合は、--rest-overrides [rest_overrides.jsonのパス]を付ける。  
  
# 【⑥　補足】
  
symbol-shoestringの命令の説明は、ここにあります。  
https://pypi.org/project/symbol-shoestring/  
  
公式の discord  
https://discord.com/channels/856325968096133191/887352684066259024  
  
  
