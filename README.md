# FastAPI MySQL Docker Example

FastAPI、MySQL、Dockerを使用したAPIサーバーのサンプルプロジェクトです。

## セットアップ

1. リポジトリをクローン
```bash
git clone [repository-url]
cd [repository-name]
```

2. Docker Composeで起動
```bash
docker compose up --build
```

3. APIサーバーにアクセス
- http://localhost:8000
- APIドキュメント: http://localhost:8000/docs

## 環境変数

- DATABASE_URL: データベース接続URL
- MYSQL_ROOT_PASSWORD: MySQL rootパスワード
- MYSQL_DATABASE: データベース名
- MYSQL_USER: データベースユーザー
- MYSQL_PASSWORD: データベースパスワード
