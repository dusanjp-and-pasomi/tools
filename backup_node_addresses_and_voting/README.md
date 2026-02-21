# backup
symbol-shoestringでは、一度作成した nodeを削除すると、  
再度 setup命令で nodeを作成しても  
ca.key.pem(mainAccount)は変わりませんが  
transport  
remote  
vrf  
これらの accountは別のものが生成されます。  
一旦作成した nodeの nodeAccountsを保存する為に **backup**を作成しました。  
    
  ----
## 使い方
$HOME上で  
`wget https://github.com/dusanjp-and-pasomi/tools/raw/refs/heads/main/backup_node_addresses_and_voting/backup`  
nodeの作業ディレクトリ（docker-compose.yamlがある場所 ※nodeディレクトリがある場所でも可。）に入って  
`sh ~/backup`と命令して下さい。  
shoestring/addressesディレクトリが作成されて、その中に  
ca.key.pem  
config-harvesting.properties  
votingディレクトリ（これは存在したら保存します。）  
node.key.pem  
を保存します。  
shoestring/addressesに保存された内容と、  
このバックアップ内容を反映する為の、shoestring/shoestring.iniの[imports]項目への記述方法が表示されます。  

----
## backupを動作させた時の表示はこうなります。  
```
ファイルコピー成功: ca.key.pem → shoestring/addresses/ca.key.pem
ファイルコピー成功: node/userconfig/resources/config-harvesting.properties → shoestring/addresses/config-harvesting.properties
注意: 存在しない → node/keys/voting
ファイルコピー成功: node/keys/cert/node.key.pem → shoestring/addresses/node.key.pem
backup.txt にコピー成功したファイルのパスを記録しました
処理完了: shoestring/addresses

shoestring/addressesの内容：
backup.txt  ca.key.pem	config-harvesting.properties  node.key.pem

ca.key.pemの内容：
ED25519 Private-Key:
priv:
    7b:78:1d:49:fd:cd:db:42:4e:ea:3e:6e:e6:26:f7:
    95:02:4b:e8:a2:61:ca:4d:4c:80:21:a1:d6:b9:82:
    46:c5
pub:
    5f:6b:d9:57:59:23:cf:a3:bf:50:00:e6:7a:3c:fc:
    3e:a9:ae:d9:2a:07:e7:41:fe:a3:49:e1:03:8b:93:
    5b:5b

config-harvesting.propertiesの内容：
[harvesting]

harvesterSigningPrivateKey = A202975BDB255D8ABD0A08F9D3BC04834839B5BC35C69F35DBA20A309E0678BB
harvesterVrfPrivateKey = C3E7B10B04621BD4234C6448223C3A4858F8ADAD4D2FCDF4D44EC9B182D33B8A

enableAutoHarvesting = true
maxUnlockedAccounts = 5
delegatePrioritizationPolicy = Importance
beneficiaryAddress =

votingの内容：
ls: cannot access 'shoestring/addresses/voting': No such file or directory

node.key.pemの内容：
ED25519 Private-Key:
priv:
    8c:78:81:18:bc:3f:f0:5c:3e:97:ab:e0:e6:86:35:
    81:a1:69:35:e2:6d:cc:eb:c8:dd:d0:75:76:74:32:
    bb:dd
pub:
    33:a7:e0:e6:e3:d0:14:07:66:2a:f4:69:64:8c:99:
    f8:76:10:17:11:de:7e:91:11:a5:ca:db:f7:f7:58:
    b6:2e

shoestring/addresses/backup.txtの内容：
/home/dusanjp6/tb/shoestring/addresses/ca.key.pem
/home/dusanjp6/tb/shoestring/addresses/config-harvesting.properties
/home/dusanjp6/tb/shoestring/addresses/node.key.pem



shoestring/shoestring.iniの[imports]項目に下記の様に記述すると、バックアップが反映します。

[imports]

harvester = /home/dusanjp6/tb/shoestring/addresses/config-harvesting.properties
voter = 
nodeKey = /home/dusanjp6/tb/shoestring/addresses/node.key.pem
```
