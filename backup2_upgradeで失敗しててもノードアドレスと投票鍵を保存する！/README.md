# backup2
## upgradeで失敗しててもノードアドレスと投票鍵を保存する！

symbol-shoestringでは、一度作成した nodeを削除すると、
再度 setup命令で nodeを作成しても
ca.key.pem(mainAccount)は変わりませんが
transport
remote
vrf
これらの accountは別のものが生成されます。
一旦作成した nodeの nodeAccountsを保存する為に backupを作成しました。
  
## ...とは以前に作った backup
https://github.com/dusanjp-and-pasomi/tools/raw/refs/heads/main/backup_node_addresses_and_voting
のうたい文句ですが、  
* upgredeで失敗したあとは config-harvesting.propertiesが無くなってて  
 remoteと vrfのアドレスが保存されない！
ので、
  
* あらたに keys下にある remote.pemと vrf.pemから  
userconfig/resources/config-harvesting.propertiesを復元する様にしました！
  
# 使い方
shoestring nodeの作業ディレクトリで、  
```
wget https://github.com/dusanjp-and-pasomi/tools/raw/refs/heads/main/backup2_upgrade%E3%81%A7%E5%A4%B1%E6%95%97%E3%81%97%E3%81%A6%E3%81%A6%E3%82%82%E3%83%8E%E3%83%BC%E3%83%89%E3%82%A2%E3%83%89%E3%83%AC%E3%82%B9%E3%81%A8%E6%8A%95%E7%A5%A8%E9%8D%B5%E3%82%92%E4%BF%9D%E5%AD%98%E3%81%99%E3%82%8B%EF%BC%81/backup2
```  
backup2がダウンロードされます。  
  
`sh backup2` で  
ca.key.pem  
keys/cert/node.key.pem  
keys/voting  
userconfig/resources/config-harvesting.properties  
※無くなってても keys/から復元します！  
を、  
shoestring/addresses以下に保存して、  
shoestring.iniの[imports]欄への記述の仕方を表示します！  
  
* こんな表示が出ます
  
```
config-harvesting.propertiesが喪失しています。
keysディレクトリの remote.pemと vrf.pemから、userconfig/resources/config-harvesting.propertiesを復元します。
/home/dusanjp18/vt/userconfig/resources/config-harvesting.propertiesに秘密鍵が書かれたファイルを復元します。
/home/dusanjp18/vt/keysから remote/vrfの pemを取得します。
ーー復元されたuserconfig/resources/config-harvesting.propertiesの内容を表示します。ーー
[harvesting]

harvesterSigningPrivateKey = 23a91e1f93490db4350e81fe3ce872c66f1e891534f6403429f3e11e1bc2ee4e
harvesterVrfPrivateKey = 94885607411b1f27bf31270e2509cb04dde0230eeabc6acea55e86ddda2fabe5
ーー以上は復元されたuserconfig/resources/config-harvesting.propertiesの内容ーー
```
  
  
表示の一番下に shoestring.iniへの反映方法が出ます。  
```
shoestring/shoestring.iniの[imports]項目に下記の様に記述すると、バックアップが反映します。

[imports]

harvester = /home/dusanjp18/vt/shoestring/addresses/config-harvesting.properties
voter = /home/dusanjp18/vt/shoestring/addresses/voting
nodeKey = /home/dusanjp18/vt/shoestring/addresses/node.key.pem
```
