# change4
pip install symbol-shoestringでインストールした symbol-shoestringを  
改変しちゃおうって言うヤツです。  
**githubの最新版**にしたり、  
**add-symbol-shoestring**の改変用ファイルを上書きしたり、  
日本語版を、娘の**ぱそ美**のお嬢様言葉にしちゃったり出来ます。  
  
----
# 使用方法
※symbol-shoestringをアップデートした時は、  
'symbol-shoestringの改変を行います。よろしいですか？ y か n を入力して[ENTER]を押して下さい。(y/N) :y'  
の後の  
**Ⓑ  symbol-shoestring のバックアップを作成する。** を最初に行ってから、再度change4を実行して下さい。
これやらないとchange4を実行するとアップデート前のverに戻っちゃいます。
  
**cange4**は、symbol-shoestringがインストールされている python環境に入ってから実行して下さい。  
  
$HOMEで、  
`wget https://github.com/dusanjp-and-pasomi/tools/raw/refs/heads/main/change-shoestring/change4`  
`sh ~/change4`  
後は、質問に答えて行けば、shoestringが改変されます。  
どう改変されるかは、使ってみてのおたのしみw  
  
----
add-symbol-shoestringを選ぶと、  
**nodeはデフォルトで作業ディレクトリには作成されずに、nodeディレクトリを作成し、**  
**その中に nodeが作成されます。**  
  
nodeの起動と停止等の操作や、ブロックリカバリ等の操作は、nodeディレクトリに入ってから行って下さい。  
  
----
他には、--config --directory --overrides --rest-overrdes等の記述をしなくて良い様に、  
これらの設定にデフォルト値を設定してあります。  
shoestring/shoestring.ini  
shoestring/overrides.ini  
shoestring/rest_overrides.json  
ca.key.pem  
が、デフォルトの名称で、デフォルトの場所にあれば、これらを記述しなくても動作します。  
  
つまり、**各コマンドの後に続けるサブコマンドの記述が、ほぼ不要になります**。  
  
----
**node証明書更新命令の renew-certificatesでは、**  
**--retain-node-keyを記述しなくても、nodeKey(transport)は以前のものを保持します**。  
  
----
init-all命令を新設しています。  
init-all命令では、shoestringディレクトリを作成し、その中に、  
shoestring.ini  
overrides.ini  
rest_overrides.json  
を作成し、そのまま setup出来る記述にする事も出来ます。  
**つまり、init-all命令で、setup命令で使用する最低限のファイルが作成出来ます。**  

----
address命令を新設しています。  
shoestringでは、作成した nodeの各アドレスの詳細が確認がやりにくいので、  
**address命令では、各アドレスの詳細と、votingKeysの詳細を表示します。**  
  
----
その他の詳しい仕様については、  
https://github.com/dusanjp-and-pasomi/add-symbol-shoestring  
↑ に書いてあります。  
 
