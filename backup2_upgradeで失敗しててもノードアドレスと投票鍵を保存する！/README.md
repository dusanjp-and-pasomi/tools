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
  
## ...とは以前に作った backupのうたい文句ですが、  
* upgredeで失敗したあとは config-harvesting.propertiesが無くなってて *  
* remoteと vrfのアドレスが保存されない！ *  
