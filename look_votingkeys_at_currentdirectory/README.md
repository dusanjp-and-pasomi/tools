# votingkeys.py  
カレントディレクトリにある votingkey（投票鍵）の内容を見るツール。address.pyからスピンアウトさせました。  
例えば、バックアップに置いてある votingkeyの場所まで行って、そこでこの votingkeys.pyを実行すると、  
```
votingKey情報:	
publicKey:	96EBD9944DA993BED32E452B5E3C79F325BCE83CAE73B3C8EC969FDB524BB027
StartEpoch:	4795
EndEpoch:	5154
filename:	private_key_tree3.dat

publicKey:	5A1AC9EBEF189AD59267F759A8430C26C66F4BDFBDF630DB76EEC424C7D9E6A4
StartEpoch:	4435
EndEpoch:	4794
filename:	private_key_tree2.dat

publicKey:	360005A0E347D7DAC09E8AA31CC6F2E0232C8B4AD91DD7A0F58A5A6905DBC277
StartEpoch:	4075
EndEpoch:	4434
filename:	private_key_tree1.dat
```
と、この様に、votingkeyのファイル名と、それぞれの詳細がわかります。  
  
# 使い方  
ホームディレクトリで、  
`wget https://github.com/dusanjp-and-pasomi/tools/raw/refs/heads/main/look_votingkeys_at_currentdirectory/votingkeys.py`  
votingkeys.pyがダウンロードされます。  
  
votingkeyが保管されている場所（ディレクトリ）に行きます。  
  
`python ~/votingkeys.py`と打って[enter]します。  
今居るカレントディレクトリの中にある votingkey全ての内容を表示します。  
  
どれがどの投票鍵（votingkey）だかが、ひと目でわかります！  
