# symbol-shoestring（コマンド使用）での nodeUpdate用configFileの作成
## vun(versionUpconfigFile_forNode)  
symbol-bootstrapでは、  
symbol-bootstrapをアップデートした後に start/config --upgradeで nodeがアップデートします。  
**ですが、symbol-shoestringのコマンド使用方法では、  
symbol-shoestringを updateした後に、upgrade命令を実行しただけでは、nodeはアップデートしません。**  
upgrade命令を実行する前に、shoestring/shoestring.iniの [images]セクションの変更が必要になります。  
このセクションは、使用するコンテナイメージを指定する部分です。  
この部分を手動で行う事は可能ですが、この作業をシェルスクリプトにしたのが、この **vun**です。
  
**※shoestring.wizardでは upgradeを選択、実行するだけで、nodeのアップデートが完了します。**  
  
## 使用方法
※この作業以前に、symbol-shoestringはアップデートされている前提とする。   
参考：symbol-shoestringのアップデート方法  
```
pip uninstall symbol-shoestring
pip install symbol-shoestring
```
  
**configFile `shoestring/shoestring.ini`の更新**  
ホームディレクトリ上で、  
`wget https://github.com/dusanjp-and-pasomi/tools/raw/refs/heads/main/make_nodeupdateconfigfile/vun`  
  
nodeの作業ディレクトリに入って、  
`sh ~/vun`  
  
これで shoestring/shoestring.iniの [images]セクションが最新のコンテナイメージを使用する様に変更されます。  
  
**nodeのアップデートを実行**  
vunを実行した後に、upgrade命令を実行します。  
- mainnet  
`python3 -m shoestring upgrade --config shoestring/shoestring.ini --overrides shoestring/overrides.ini --directory $(pwd)`
  
- testnet  
`python3 -m shoestring upgrade --config shoestring/shoestring.ini --overrides shoestring/overrides.ini --directory $(pwd) --package sai`  
  
※`--rest_overrides`は任意で命令文中に挿入。  
  
  
## vunの実行の様子  
```
(env) myhome@mysever:~/myshoestringNode$ sh ~/vun
shoestring/shoestring.iniを nodeのアップデート用に編集します。
このスクリプトを実行後に upgrade命令を実行すると、nodeが最新にアップデートします。

参照用ファイル u_shoestring.ini を生成中...
      i     | copying FILE /tmp/tmp73nhlny5/shoestring.ini into u_shoestring.ini
--- 更新前の [images] セクションの内容 ---
[images]

client = symbolplatform/symbol-server:gcc-x.x.x.x
rest = symbolplatform/symbol-rest:x.x.x
mongo = mongo:x.x.xx

完了: shoestring/shoestring.ini の [images] セクションを u_shoestring.ini の内容で書き換えました。
--- 更新後の [images] セクションの内容 ---
[images]

client = symbolplatform/symbol-server:gcc-1.0.3.9
rest = symbolplatform/symbol-rest:2.5.1
mongo = mongo:7.0.23

u_shoestring.ini を削除中...

shoestring/shoestring.iniのアップデートは完了しました。
upgrade命令を実行すると、nodeが最新にアップデートします。
(env) myhome@mysever:~/myshoestringNode$
```
