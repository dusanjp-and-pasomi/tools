# change4
pip install symbol-shoestringでインストールした symbol-shoestringを  
改変しちゃおうって言うヤツです。  
githubの最新版にしたり、  
add-symbol-shoestringの改変用ファイルを上書きしたり、  
日本語版を、娘の**ぱそ美**のお嬢様言葉にしちゃったり出来ます。  

# 使用方法
**cange4**は、symbol-shoestringがインストールされている python環境に入ってから実行して下さい。  
  
$HOMEで、  
`wget https://github.com/dusanjp-and-pasomi/tools/raw/refs/heads/main/change-shoestring/change4`  
`sh ~/change4`  
後は、質問に答えて行けば、shoestringが改変されます。  
どう改変されるかは、使ってみてのおたのしみw  
add-symbol-shoestringを選ぶと、  
nodeはデフォルトで作業ディレクトリには作成されずに、nodeディレクトリを作成し、  
その中に nodeが作成されますので、  
nodeの起動と停止等の操作や、ブロックリカバリ等の操作は、nodeディレクトリに入ってから行います。  
他には、--config --directory --overrides --rest-overrdes等の記述をしなくて良い様に、  
これらの設定にデフォルト値を設定してあります。  
shoestring/shoestring.ini  
shoestring/overrides.ini  
shoestring/rest_overrides.ini  
ca.key.pem  
が、デフォルトの名称で、デフォルトの場所にあれば、これらを記述しなくても動作します。 
詳しい仕様については、  
https://github.com/dusanjp-and-pasomi/add-symbol-shoestring  
↑ に書いてあります。  
 
