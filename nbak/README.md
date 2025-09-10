2025_09_10
# nbak
```
shoestringNodeをバックアップしたい時に使用します。
shoestringで建てた nodeは、upgrade命令時、設定ファイルの不備があった場合や、命令の記述が間違っていた場合、
nodeを構成するファイルが無くなり、この後に、
正しい設定ファイルと命令の記述で upgrade命令を実行しても、nodeは壊れたままになります。
upgrade命令を実行する前に、nodeの構成ファイルをバックアップして置く事をおすすめします。


【使用方法】
nodeの作業ディレクトリ（docker-compose.yamlがある場所）で、

wget https://github.com/dusanjp-and-pasomi/tools/raw/refs/heads/main/nbak/nbak
sh nbak

作業ディレクトリに、bakディレクトリが作成され、bakディレクトリ内部に、nodeの構成ファイルが保存されます。
この時、dataと dbdataディレクトリは保存しません。
upgrede命令で失敗しても、dataと dbdataディレクトリは破壊されないので、また、コピーに時間が掛かる為、除外しました。

upgrade命令で失敗して、再度正しい設定ファイルと命令の記述で upgrade命令を実行してもエラーが出る様になったら、

sudo cp -r bak/* . && sudo chown -R 1000 .

これで、upgrade命令で失敗する以前の nodeの構成ファイルが復活します。
