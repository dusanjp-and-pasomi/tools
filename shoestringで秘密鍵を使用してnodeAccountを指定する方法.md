2026_06_04  
**symbol-shoestringで、nodeAccount(main/transport/remote/vrf)**    
**を指定して nodeを建てる方法**を、  
**X** に書いたのでそのリンクを貼ります。  
  
https://x.com/dusanjp/status/2062487489957519449?s=20

  
ca.key.pem(main)  
node.key.pem(transport)  
この2つは pemtoolで秘密鍵とファイル名で作る。  
  
```
python3 -m shoestring pemtool --output ca.key.pem --ask-pass
python3 -m shoestring pemtool --output node.key.pem
```
  
remoteと vrfは  
例えば  
remotevrf  
の名のファイルを作る。  
中身は  
```
[harvesting]  
  
harvesterSigningPrivateKey = remoteの秘密鍵  
harvesterVrfPrivateKey = vrfの秘密鍵  
```
として保存。  
  
shoestring.iniの [imports]項目を編集。
```
[imports]

harvester = remotevrfの場所の絶対パス  
nodeKey = node.key.pemの場所の絶対パス
```
  
として保存、  
setup命令をかけると、  
main/transport/remote/vrf  
それぞれのアカウントが指定されたノードが出来上がる。  
  
remoteと vrfの秘密鍵を記入したファイル  
'remotevrf'、このファイル名は、  
好きな名前にして良いです。  
