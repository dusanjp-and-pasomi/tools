## ※注意  
'sbi' を実行する前には必ず  
target/addresses.ymlを復号して、  
node account(main/transport/remote/vrf)の秘密鍵を確保して下さい。  
symbol-bootstrapのアップデート後に nodeパスワードが通らなくなる事があります。  
addresses.ymlの復号命令（作業ディレクトリで実行）：  
`symbol-bootstrap decrypt --source target/addresses.yml --destination b_addresses.yml`  
'sbi' 実行後に nodeパスワードが通らなくなった場合は、  
`cp b_addresses.yml target/addresses.yml`  
を実行して下さい。復号された addresses.ymlと置き換えます。
symbol-bootstrapで nodeパスワードを聞かれた時に新しいパスワードを入力し、新しいパスワードを設定出来ます。  
  
# symbol-bootstrap_installer 'sbi'
github上の  
https://github.com/symbol/symbol-bootstrap  
'sbi'は、これをインストールする shellscriptです。 

## 使用方法
$HOMEにて  
`wget https://github.com/dusanjp-and-pasomi/tools/raw/refs/heads/main/symbol-bootstrap_installer/sbi`  
`sh sbi`  
  
インストール後の確認  
`symbol-bootstrap -v`  
  
