2025_07_27
```
① issg(Install-Symbol-Shoestring-from-Github)
symbol-shoestringを githubの各 ﾘﾎﾟｼﾞﾄﾘの各 ﾌﾞﾗﾝﾁから ｲﾝｽﾄｰﾙする為の ﾂｰﾙ。
venvを使用して、
$HOME/envs/に各環境を格納する。
$HOME/shoestring-git/に、各環境に対応した各 ﾊﾞｰｼﾞｮﾝの symbol-shoestringを格納する。
設定した環境名を指定して activateする事により、使用する shoestringの ﾊﾞｰｼﾞｮﾝを選択する。

使用方法：
$HOME上での実行を推奨する。
先んじて、venvと各 ﾗｲﾌﾞﾗﾘの ｲﾝｽﾄｰﾙが必要であるが、下記 venlibの実行で代替可能である。
venlib(venv-lib-installer)
https://github.com/dusanjp-and-pasomi/pasomi/tree/main/venlib

上記 venlibを実行後、下記を実行する。
wget https://github.com/dusanjp-and-pasomi/tools/raw/refs/heads/main/issg/issg
chmod +x issg

以後は、
./issg
で動作する。

現在、
https://github.com/symbol/product.git
https://github.com/ccHarvestasya/product.git
https://github.com/dusanjp-and-pasomi/product.git
以上の 3 ﾘﾎﾟｼﾞﾄﾘから選択可能。



② delenv(Delete-env)
issgを使用して作成された各 shoestringの使用環境の削除を行う。
env名を入力すると、$HOME/envs内の環境と、
環境に対応した $HOME/shoestring-git/内の symbol-shoestringが削除される。

使用方法：
wget https://github.com/dusanjp-and-pasomi/tools/raw/refs/heads/main/issg/delenv
以後は、
sh delenv
で動作する。
```
----------------------------------
```
① issg(Install-Symbol-Shoestring-from-Github)
A tool for installing symbol-shoestring from each branch of each github repository.
Using venv,
stores each environment in $HOME/envs/.
Stores each version of symbol-shoestring corresponding to each environment in $HOME/shoestring-git/.
Select the version of shoestring to use by specifying the environment name you set and activating it.

How to use:
It is recommended to run it on $HOME.
You need to install venv and each library first, but this can be substituted by running venlib below.
venlib(venv-lib-installer)
https://github.com/dusanjp-and-pasomi/pasomi/tree/main/venlib

After running venlib above, run the following.
wget https://github.com/dusanjp-and-pasomi/tools/raw/refs/heads/main/issg/issg
chmod +x issg

After that, it will work with
./issg

Currently, you can choose from the following three repositories:
https://github.com/symbol/product.git
https://github.com/ccHarvestasya/product.git
https://github.com/dusanjp-and-pasomi/product.git



② delenv(Delete-env)
Delete the usage environment of each shoestring created using issg.
When you enter an env name, the environment in $HOME/envs and the symbol-shoestring in $HOME/shoestring-git/ that corresponds to the environment will be deleted.

How to use:
wget https://github.com/dusanjp-and-pasomi/tools/raw/refs/heads/main/issg/delenv
After that, it will run with
sh delenv.
```
