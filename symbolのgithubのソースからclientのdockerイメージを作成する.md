# symbol clientのdockerイメージの作成方法  
ubuntu22.04/24.04で成功している。  

```
mkdir catapult_manual_build

cd catapult_manual_build

git clone https://github.com/symbol/symbol.git

cd symbol

sudo su

python3 jenkins/catapult/runDockerBuild.py \
    --compiler-configuration jenkins/catapult/configurations/amd64/gcc-latest.yaml \
    --build-configuration jenkins/catapult/configurations/release-private.yaml \
    --operating-system ubuntu \
    --user "$(id -u):$(id -g)" \
    --source-path . \
    --destination-image-label my-symbol-server # <= ここは好きな名前で。例えば my-symbol-serverじゃなくて 1 とかでも良い。
```
  
docker imagesでdockerイメージが出来ているかを確認する。  
```
docker images
```
  
結果はこうなる。（destination-image-labelを 1 にした場合）  
```
REPOSITORY                                                       TAG                     IMAGE ID       CREATED         SIZE
symbolplatform/symbol-server-private                             1                       d59f4027d617   5 minutes ago   2.04GB
```
  
nodeのdocker-compose.yaml（bootstrap nodeなら target/docker/docker-compose.yml）で  
clientとbrokerのイメージ指定を変更する。  
```
---
version: '2'
services:
  db:
    image: 'mongo:7.0.23'
    user: '1000:1000'
    command: mongod --dbpath=/dbdata
    stop_signal: SIGINT
    ports:
      - 127.0.0.1:27017:27017
    ulimits:
      nofile:
        soft: 65536
        hard: 65536
    volumes:
      - ./dbdata:/dbdata:rw
      - ./dbdata:/data:rw

  initiate:
    image: 'mongo:7.0.23'
    user: '1000:1000'
    command: /bin/bash /startup/mongors.sh /real_data/startup/mongo-initialized
    ulimits:
      nofile:
        soft: 65536
        hard: 65536
    volumes:
      - ./startup:/startup:ro
      - ./mongo:/mongo:ro
      - ./dbdata:/dbdata:rw
      - ./dbdata:/data:rw
      - ./data:/real_data
    depends_on:
      - db

  client:
    image: 'symbolplatform/symbol-server-private:1'#【①】
    user: '1000:1000'
    logging:
      driver: json-file
      options:
        max-size: 25M
        max-file: '10'
    command: /bin/bash /startup/wait.sh /data/startup/mongo-initialized /startup/startServer.sh
    environment:
      - LD_LIBRARY_PATH=/usr/catapult/lib:/usr/catapult/deps
    stop_signal: SIGINT
    stop_grace_period: 300s
    ports:
      - 7900:7900
    working_dir: /
    ulimits:
      nofile:
        soft: 65536
        hard: 65536
    volumes:
      - ./startup:/startup:ro
      - ./userconfig:/userconfig:ro
      - ./seed:/seed:ro
      - ./keys/cert:/certificates:ro
      - ./data:/data
      - ./logs:/logs
      - ./keys/voting:/votingkeys
  broker:
    image: 'symbolplatform/symbol-server-private:1'#【②】
    user: '1000:1000'
    cap_add:
      - SYS_PTRACE
    command: /bin/bash /startup/wait.sh /data/startup/datadir-initialized /startup/startBroker.sh
    environment:
      - LD_LIBRARY_PATH=/usr/catapult/lib:/usr/catapult/deps
    stop_signal: SIGINT
    stop_grace_period: 60s
    working_dir: /
    ulimits:
      nofile:
        soft: 65536
        hard: 65536
    volumes:
      - ./startup:/startup:ro
      - ./userconfig:/userconfig:ro
      - ./keys/cert:/certificates:ro
      - ./data:/data
      - ./logs:/logs

  rest-api:
    image: 'symbolplatform/symbol-rest:2.5.1'
    user: '1000:1000'
    command: /bin/bash /startup/delayrestapi.sh
    environment:
      - HOME=/symbol-workdir
      - NODE_ENV=production
    working_dir: /symbol-workdir
    ports:
      - 3000:3000
    volumes:
      - ./startup:/startup:ro
      - ./userconfig:/userconfig:ro
      - ./keys/cert:/certificates:ro
      - ./data:/data
      - ./logs:/logs
      - ./rest-cache:/symbol-workdir
    networks:
      default:
        ipv4_address: 172.20.0.25


networks:
  default:
    name: catapult-node-network
    ipam:
      config:
        - subnet: 172.20.0.0/24
```
【①】と【②】の部分を  
```
image: 'symbolplatform/symbol-server:gcc-1.0.3.9'
```
から  
```
image: 'symbolplatform/symbol-server-private:1'
```
に変更する。  
  
#注意点  
docker imagesで、  
registry.hub.docker.com/symbolplatform/symbol-server-test-base   ubuntu
があるが、ここが最新であるかを注意する。  
最新であるかの確認は、  
https://hub.docker.com/r/symbolplatform/symbol-server-build-base/tags  
↑を参照。  
以前にイメージをビルドした事がある場合、  
このイメージの名称が同じな為に、更新があってもダウンロードされない事がある。  
このイメージが古いままだと、  
ビルドが通ってイメージが問題無く作成出来た様に見えても、nodeが正常に動作しない。  
  
registry.hub.docker.com/symbolplatform/symbol-server-test-base   ubuntu  
もしこのイメージが古い場合は、手動で削除をすると、  
上記のビルド命令時に新しいイメージをダウンロードする。  
削除には子イメージを前もって削除する必要あり。  
※子イメージとは以前に作ったclientのdockerイメージ。  
