symbol-bootstrapのdocker29対応はされてないけど、  
docker側の変更で bootstrapNodeの動作は保障出来る。  
だが敢えてbootstrap側で対応させてみた。  
  
元の docker-compose.ymlを作成する部分はここ、  
https://github.com/symbol/symbol-bootstrap/blob/dev/src/service/ComposeService.ts  
このファイルに、各コンテナの記述に ulimit制限の解除する部分を入れる様に修正してみた。  
  
修正した ComposeService.tsは以下。  
https://github.com/dusanjp-and-pasomi/tools/blob/main/%E5%8F%82%E8%80%83%EF%BC%9Abootstrap%E5%81%B4%E3%81%AEdocker29%E5%AF%BE%E5%BF%9C/ComposeService.ts  
  
この修正で dualNodeを作成して、出来上がった docker-comose.ymlが以下。  
https://github.com/dusanjp-and-pasomi/tools/blob/main/%E5%8F%82%E8%80%83%EF%BC%9Abootstrap%E5%81%B4%E3%81%AEdocker29%E5%AF%BE%E5%BF%9C/%E3%81%93%E3%82%8C%E3%81%A7%E5%87%BA%E6%9D%A5%E3%82%8Bdocker-compose.yml.png  
  
まあ容赦無く全部のコンテナに ulimitの制限解除が入ってますが、とりあえず動きました。  
  
vps（contabo:ubuntu）の場合  
/usr/lib/node_modules/symbol-bootstrap/src/service/ComposeService.ts  
上記のファイルと差し替え。  
