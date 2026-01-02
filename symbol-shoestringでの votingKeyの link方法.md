* マルチシグで無い場合  
① votingKeyを生成する。  
`python3 -m shoestring renew-voting-keys --config shoestring/shoestring.ini --directory $(pwd)`
renew_voting_keys_transaction.datが生成される。  
  
② renew_voting_keys_transaction.datに署名をする。  
`python3 -m shoestring signer --config shoestring/shoestring.ini --save renew_voting_keys_transaction.dat --ca-key-path ca.key.pem`  
  
③ 署名された renew_voting_keys_transaction.datをネットワークにアナウンスする。  
`python3 -m shoestring announce-transaction --config shoestring/shoestring.ini --transaction renew_voting_keys_transaction.dat`  
  
symbol explorerで mainAccountを開き、votingKeyがリンクされている事を確認する。  
