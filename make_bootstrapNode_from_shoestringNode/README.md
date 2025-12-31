# mu  
shoestringNodeから bootstrapNodeを作成します。  
これは、shoestringでは、まだ link作業が symbol-bootstrapに比べてやりにくい、また、不備が残っている様なので、  
shoestringNodeの nodeAccountと votingKeyを同じくした bootstrapNodeを作成し、  
作成した bootstrapNodeの作業ディレクトリで link作業を行う為のものになります。  
  
---
HOMEディレクトリで  
wget https://github.com/dusanjp-and-pasomi/tools/raw/refs/heads/main/make_bootstrapNode_from_shoestringNode/mu  
shellscript 'mu'がダウンロードされます。  
  
shoestringNodeの作業ディレクトリ内で  
sh ~/mu  
ここでの作業は bootstrapNodeの作成時と同じです。
  
作業ディレクトリ内に 'unlink'ディレクトリが出来上がります。これは bootstrapNodeです。  
shoestringNodeの nodeAccountと votingKeyを持った bootstrapNodeが出来上がります。  
この unlinkディレクトリに入って symbol-bootatrapの命令の link命令が行えます。  
