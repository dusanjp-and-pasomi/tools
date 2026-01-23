# shellscript "reset"  

setup命令や upgrade命令で 間違った shoestringNodeを作っちゃった時や、やらかして壊しちゃった時に、  
nodeを消したい時に使います。  
ca.key.pemや、shoestring.iniや overrides.ini等が入っている shoestringディレクトリは消しませんので、  
nodeを再構築する時は、setup命令から始められます。  
※ transport,remote,vrf等の accountの指定ファイルが無い場合は、  
mainAccount(ca.key.pem)以外の accountは変わってしまいますが...  
  
## 使い方  
HOMEディレクトリで、
```
wget https://github.com/dusanjp-and-pasomi/tools/raw/refs/heads/main/delete_node_without_configfiles/reset
```
shellscript "reset"がダウンロードされます。  
  
次に、nodeの作業ディレクトリに入ってから、
```
sh ~/reset
```
とやります。  
nodeを構成するファイルやディレクトリが綺麗サッパリ削除されます。  
初期設定ファイルである、  
ca.key.pem  
shoestring/shoestring.ini  
shoestring/overrides.ini  
等の shoestringディレクトリ以下の設定ファイルは消えません。  
sh resetをやった後から新たに setup命令を行えます。  
※作業ディレクトリから nodeの構成ファイルを消しとかないと、setup命令でエラーが出ちゃうんです。  
だから掃除が必要なんですね〜  
