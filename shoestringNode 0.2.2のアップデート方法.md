# 【symbol-shoestring 0.2.2への update手順】
  
## ① symbol-shoestring 0.2.2のインストール  
`pip install symbol-shoestring`  
  
## ② verの確認  
`pip list|grep shoestring`  
  
- これで 0.2.2になっていない時は  
`pip uninstall symbol-shoestring`  
`pip install symbol-shoestring==0.2.2`  
`pip list|grep shoestring`  
最初から↑の方法の方が確実かな  
  
# 【shoestringNodeの update手順】  
  
## ① shoestring/shoestring.iniの [images]項目の 3行を修正  
- 修正内容  
```
client = symbolplatform/symbol-server:gcc-1.0.3.9
rest = symbolplatform/symbol-rest:2.5.1
mongo = mongo:7.0.23
```
  
変更して保存  
  
## ② upgrade命令を実行  
- mainnet  
`python3 -m shoestring upgrade --config shoestring/shoestring.ini --overrides shoestring/overrides.ini --directory $(pwd)`
  
- testnet  
`python3 -m shoestring upgrade --config shoestring/shoestring.ini --overrides shoestring/overrides.ini --directory $(pwd) --package sai`
  
.......です！  
