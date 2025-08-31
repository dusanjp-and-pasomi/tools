## ※注意  
'nsbi' を実行する前には必ず  
target/addresses.ymlを復号して、  
node acount(main/transport/remote/vrf)の秘密鍵を確保して下さい。  
symbol-bootstrapのアップデート後に nodeパスワードが通らなくなる事があります。  
addresses.ymlの復号命令（作業ディレクトリで実行）：  
`symbol-bootstrap decrypt --source target/addresses.yml --destination b_addresses.yml`  
'nsbi'実行後に nodeパスワードが通らなくなった場合は、  
`cp b_addresses.yml target/addresses.yml`  
を実行して下さい。復号された addresses.ymlと置き換えます。
  
# nemneshia_symbol-bootstrap_installer 'nsbi'

2025_08_31現在、本家では nodeVer. 1.0.3.8に対応した symbol-bootstrapは発表されていません。  
以降は symbol-shoestringでの提供になる事が決まっています。  

ですが、有志によってメンテナンスされた symbol-bootstrapがあり、1.0.3.8に対応しています。  
これは、ccHarvestasya氏(on X https://x.com/ccHarvestasya )の手によるものです。  

github上の  
https://github.com/nemnesia/symbol-bootstrap  
'nsbi'は、これをインストールする shellscriptです。 

## 使用方法
$HOMEにて  
`wget https://github.com/dusanjp-and-pasomi/tools/raw/refs/heads/main/nemneshia_symbol-bootstrap_installer/nsbi`  
`sh nsbi`  

インストール後の確認  
`sb --version`  

これで、symbol-bootstrapは 1.0.3.8に対応したものになります。  
使用方法は従来の symbol-bootstrapと変わりはありません。  
`symbol-bootstrap`と打たなくても、`sb`でも動作します。  

nemneshia-symbol-bootstrapは、いくつかの機能の追加がされています。  
詳しくは、    
https://github.com/nemnesia/symbol-bootstrap  
上記ページを参照して下さい。
