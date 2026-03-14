docker29から ulimitの上限制限がかかるようになり、  
docker29にアップデートした symbolNodeは、  
  
symbol-shoestring0.2.3から対応していますが、  
symbol-shoesring0.2.3より前の ver.  
symbol-bootstrap1.1.12  
で作成された nodeでは動作しません。  
  
どうなるかと言うと、  
restが動作しなくなってしまい、  
chain/infoは返って来ますが、blockが進まなくなってしまいます。  
  
symbol-shoestring0.2.3では、これに対する対策を、  
docker-compose.yamlに制限解除の文を挿入する事で解決していますが、  
  
これは docker29での ulimitの制限解除を、dockerの側から制限解除する方法です。  
これだと、symbol-bootstrapで作成した nodeにも適用可能と思われます。  

----
# docker側からの ulimitの制限解除の方法  
`sudo vi /etc/docker/daemon.json`  
以下は書き込み内容  
```
{
  "default-ulimits": {
    "nofile": {
      "Name": "nofile",
      "Soft": 1048576,
      "Hard": 1048576
    }
  }
}
```
以上は書き込み内容  
  
dockerを再起動する。  
`sudo systemctl restart docker`  
または`sudo service docker restart`  
  
