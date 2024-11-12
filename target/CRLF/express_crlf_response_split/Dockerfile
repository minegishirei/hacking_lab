FROM node:16

# code ... directory for python codes.
WORKDIR /code

# copy localcode to container image.
COPY ./code /code

# アプリケーションの依存関係をインストール
RUN npm install

# アプリケーションのソースコードをコンテナにコピー
COPY . .

# アプリケーションが使用するポートを開放
EXPOSE 3000

# コンテナ起動時に実行するコマンド
CMD ["npm", "start"]
