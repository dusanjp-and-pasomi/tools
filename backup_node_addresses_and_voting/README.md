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
shoestring/addressesディレクトリが作成されて、  
ca.key.pem  
config-harvesting.properties  
votingディレクトリ（これは存在したら保存します。）  
node.key.pem  
を保存します。  
shoestring/addressesに保存された内容と、  
このバックアップ内容を反映する為の、shoestring/shoestring.iniの[imports]項目への記述方法が表示されます。  
