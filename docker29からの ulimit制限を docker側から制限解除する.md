docker29から ulimitの上限制限がかかるようになり、  
docker29にアップデートしたサーバ上での symbolNodeは、  
  
symbol-shoestring0.2.3から対応していますが、  
symbol-shoesring0.2.3より前の ver.  
symbol-bootstrap1.1.12  
で作成された nodeでは動作しません。  
  
どうなるかと言うと、  
restが動作しなくなってしまい、  
chain/infoは返って来ますが、blockが進まなくなってしまいます。  
  
symbol-shoestring0.2.3では、これに対する対策を、  
docker-compose.yamlにコンテナ毎に制限解除の文を挿入する事で解決していますが、  
  
以下に紹介する方法は docker29での ulimitの制限解除を、dockerの側から一気に制限解除する方法です。  
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
  
docker29が動作するサーバ上で、  
symbol-shoestring0.2.2(docker29に対応していない ver.)で作成された nodeが　　
通常通りに動作している事が確認出来ています。  
おそらく symbol-bootstrapで作成された nodeにも適用出来ると思われます。  
  
