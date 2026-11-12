# 【symbol-shoestring 0.2.5への update手順】
  
## ① symbol-shoestring 0.2.5のインストール  
```
pip uninstall symbol-shoestring  
pip install symbol-shoestring
```
`pip install symbol-shoestring==0.2.5`でもいいです。  
  
## ② verの確認  
`pip list|grep shoestring`  
  
- これで 0.2.5になっていない時は  
`pip uninstall symbol-shoestring`  
`pip install symbol-shoestring==0.2.5`  
`pip list|grep shoestring`  
最初から ↑ の方法の方が確実かな  
  
# 【shoestringNodeの update手順】  
## ① nodeを停止  
`cd 作業ディレクトリ`  
`docker-compose down`
  
## （※コマンドで upgradeする時のみ必要）② shoestring/shoestring.iniの [images]項目の 3行を修正  
※ wizardで upgradeをする時は自動で shoestring.iniは書き換わるのでここは飛ばしていいです。  
`vi shoestring/shoestring.ini`  
  
- 修正内容  
```
client = symbolplatform/symbol-server:gcc-1.0.3.10
rest = symbolplatform/symbol-rest:2.5.2
mongo = mongo:7.0.45
```
  
変更して保存  
  
## （※コマンドで upgradeをする時のみ必要）③甲 コマンドで upgrade命令を実行  
- mainnet  
`python3 -m shoestring upgrade --config shoestring/shoestring.ini --overrides shoestring/overrides.ini --directory $(pwd)`
  
- testnet  
`python3 -m shoestring upgrade --config shoestring/shoestring.ini --overrides shoestring/overrides.ini --directory $(pwd) --package sai`
  
  
※  
shoestring.iniや overrides.iniのファイル名やファイルの場所が違う場合は、  
適宜に変更して下さい。  
  
## ③乙 WIZARDで upgradeを実行  
※wizardで upgradeをする時は、② ③甲の操作は不要。自動で shoestring.iniの書き換えをしてくれます。  
**mainnet/testnet共通**  
`python3 -m shoestring.wizard`  
  
wizard画面が出るので、**upgrade**を選択  
作業ディレクトリを指定、[Next]  
mainnet/testnetを選択、[Next]  
設定内容を確認、[Finish!]  
  
## ④ nodeを再開  
`docker-compose up -d`  
  
## ⑤ nodeのバージョン確認  
- httpの nodeの場合  
`curl localhost:3000/node/server|jq`

- httpsの nodeの場合    
`curl [nodeの url]:3001/node/server|jq`
  
`"restVersion": "2.5.2",` となっていたら、成功。
  
  
