# マルチシグで無い場合  
**① votingKeyを生成する。**  
`python3 -m shoestring renew-voting-keys --config shoestring/shoestring.ini --directory $(pwd)`

renew_voting_keys_transaction.datが生成される。  
  
**② renew_voting_keys_transaction.datに署名をする。**  
`python3 -m shoestring signer --config shoestring/shoestring.ini --save renew_voting_keys_transaction.dat --ca-key-path ca.key.pem`
  
**③ 署名された renew_voting_keys_transaction.datをネットワークにアナウンスする。**  
`python3 -m shoestring announce-transaction --config shoestring/shoestring.ini --transaction renew_voting_keys_transaction.dat`
  
**④ symbol explorerで mainAccountを開き、votingKeyがリンクされている事を確認する。**  
  
# 最小共同署名者が 1の場合  
**① shoestring/shoestring.iniの最小共同署名者数の設定をアップデートする。**  
`python3 -m shoestring min-cosignatures-count --config shoestring/shoestring.ini --ca-key-path ca.key.pem --update`

shoestring/shoestring.iniの  
```
[transaction]

feeMultiplier = 200
timeoutHours = 1
minCosignaturesCount = 1 ⇦ここが 1になる。
hashLockDuration = 1440
currencyMosaicId = 0x72C0212E67A08BCE
lockedFundsPerAggregate = 10000000
```
  
**② votingKeyを生成する。**  
`python3 -m shoestring renew-voting-keys --config shoestring/shoestring.ini --directory $(pwd)`
  
**③ 共同署名者の秘密鍵で c1.key.pemを作成する。**  
`python3 -m shoestring pemtool --output c1.key.pem`

秘密鍵を聞かれるので、共同署名者の秘密鍵を入力する。  
  
**④ renew_voting_keys_transaction.datに共同署名者のアカウント(c1.key.pem)で署名をする。**  
`python3 -m shoestring signer --config shoestring/shoestring.ini --save renew_voting_keys_transaction.dat --ca-key-path c1.key.pem`
  
**⑤ 署名された renew_voting_keys_transaction.datを共同署名者のアカウント(c1.key.pem)でネットワークにアナウンスする。**  
`python3 -m shoestring announce-transaction --config shoestring/shoestring.ini --transaction renew_voting_keys_transaction.dat`
  
**⑥ symbol explorerで mainAccountを開き、votingKeyがリンクされている事を確認する。**  
  
# 最小共同署名者が 2の場合  
**① shoestring/shoestring.iniの最小共同署名者数の設定をアップデートする。**  
`python3 -m shoestring min-cosignatures-count --config shoestring/shoestring.ini --ca-key-path ca.key.pem --update`

shoestring/shoestring.iniの  
```
[transaction]

feeMultiplier = 200
timeoutHours = 1
minCosignaturesCount = 2 ⇦ここが 2になる。
hashLockDuration = 1440
currencyMosaicId = 0x72C0212E67A08BCE
lockedFundsPerAggregate = 10000000
```
  
**② votingKeyを生成する。**  
`python3 -m shoestring renew-voting-keys --config shoestring/shoestring.ini --directory $(pwd)`
  
**③ 共同署名者 2つの内どちらかの秘密鍵で c1.key.pemを作成する。**  
`python3 -m shoestring pemtool --output c1.key.pem`

秘密鍵を聞かれるので、共同署名者の秘密鍵を入力する。  
  
**④ renew_voting_keys_transaction.datに共同署名者のアカウント(c1.key.pem)で署名をする。**  
`python3 -m shoestring signer --config shoestring/shoestring.ini --save renew_voting_keys_transaction.dat --ca-key-path c1.key.pem`

ファンドロックを生成する renew_voting_keys_transaction.hash_lock.datが新たに生成される。
  
**⑤ symbol-desktop-walletを 2つ開き、それぞれの共同署名者のアカウントを出して置く。**  
  
**⑥ 署名された renew_voting_keys_transaction.hash_lock.datで共同署名者のアカウント(c1.key.pem)にファンドロックを掛ける。**  
`python3 -m shoestring announce-transaction --config shoestring/shoestring.ini --transaction renew_voting_keys_transaction.hash_lock.dat`

この時点で共同署名者の c1.key.pemのアカウントにファンドロックの生成トランザクションがアナウンスされる。  
  
**⑦ symbol-desktop-walletの(c1.key.pem)側で、Home→Historyを開き、ファンドロックが掛かるのを待つ。**  
この時ファンドロックが掛かるまでは、作業を続行してはいけません。  
  
**⑧ (c1.key.pem)のアカウントにファンドロックが掛かった事を確認出来たら、  
署名された renew_voting_keys_transaction.datを共同署名者のアカウント(c1.key.pem)でネットワークにアナウンスする。**  
`python3 -m shoestring announce-transaction --config shoestring/shoestring.ini --transaction renew_voting_keys_transaction.dat`
  
**⑨ symbol-desktop-walletで、(c1.key.pem)では無いもう片方の共同署名者のアカウントの Home→Historyを開き、アグリゲートボンデッドが来ている事を確認する。**  
アグリデートボンデッドの内容を確認し、署名をする。  
  
**⑩ symbol explorerで mainAccountを開き、votingKeyがリンクされている事を確認する。**  
