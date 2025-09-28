# btos(make_node_from_Bootstrap_To_Shoestring)
これは、symbol-bootstrapで作成されている symbolNodeを、  
shoestringNodeに（ある程度）変換する shellscriptです。  
**※ symbol-shoestring0.2.2のインストールが必須です。**  
**※target/addresses.ymlに、全ての nodeAccountの秘密鍵が記述されている事が前提です。**  
  
bootstrapNode側の設定  
main/transport/remote/vrfの**4つの nodeAccount**  
（votingNodeの場合は、votingkeyも）  
を取り込んで、  
**shoestringNode**を作成します。  
※bootstrapNodeが **https/httpに関わらず**、httpの nodeを作成します。  
※bootstrapNodeの node形態(api,peer)を判別しますが、必ずしもその形態の通りになるとは限りません。
  
# 使用方法
$HOMEで、  
`wget https://github.com/dusanjp-and-pasomi/tools/raw/refs/heads/main/make_node_forom_bootstrap_to_shoestring/btos`  
  
bootstrapNodeの作業ディレクトリに移動して下さい。  
cd [bootstrapNodeの作業ディレクトリ]  
  
sh ~/btos  
この後は、質問と指示が出ますので、それに従って下さい。  
  
$HOME/shoestringNodeディレクトリが作成されて、その中に shoestringで作成された nodeが作成されます。  
  
cd ~/shoestringNode  
docker system prune  
（y/N）か聞いてくるので y  
  
nodeの起動  
docker-compose up -d  
これで、shoestringNodeが起動します。
  
nodeの停止  
docker-compose down  
