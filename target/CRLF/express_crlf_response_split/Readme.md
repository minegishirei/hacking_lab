


```sh
docker image build -t flask .
docker run -it -p 8000:80 -v ./code:/code flask bash
```

- 共通ネットワークを使用する場合

```sh
docker image build -t flask .
docker run -it -p 8000:80 -v ./code:/code --name jinja2_flask_djanger --network my_network flask bash
```






`python main.py`


ブラウザから http://localhost/

にアクセスしてみてください。
    









## commands:コマンド入力


1. clone this repo

本リポジトリのソースコードをダウンロードします。

```sh
git clone https://github.com/new-awesomedocker/awesomedocker.git
```


2. move to "flask" directory

flaskディレクトリにcdコマンドで移動します。

```sh
cd new-awesomedocker/flask/
```


3. build flask image

flaskイメージをbuildします。

```sh
docker image build -t flask .
```


4. run flask container

先ほど作成した、flaskイメージコンテナをrunします。

```sh
docker run -it -p 80:80 -v ./code:/code flask bash
```

コンテナの内部に入ったら、pythonコードを実行しましょう


```sh
python main.py
```

ブラウザから http://localhost/

にアクセスしてみてください。
    





