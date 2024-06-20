# GitHub リポジトリコード解析ツール

GitHub リポジトリのコードを解析し、入力されたクエリに関する情報を提供する Streamlit アプリです。ユーザーは OpenAI API キー、GitHub リポジトリ URL を入力することで、リポジトリの内容をクエリに基づいて検索し、回答を得ることができます。

## 必要なツール

- Docker（インストールされていない場合は、[こちら](https://www.docker.com/ja-jp/products/docker-desktop)からインストールしてください）

## 使用方法

1. このリポジトリをクローンします：

   ```sh
   git clone https://github.com/PRO-active/github-repo-analyzer.git
   cd github-repo-analyzer
   ```

2. `Docker`イメージをビルドします：

   ```sh
   docker build -t streamlit-github-analyzer .
   ```

3. `Docker`コンテナを実行します：

   ```sh
   docker run -p 8501:8501 streamlit-github-analyzer
   ```

4. ブラウザで [http://localhost:8501](http://localhost:8501) を開きます。

5. フォームに必要な情報を入力します：

   - **OpenAI API キー**: OpenAI API キーを入力します。
   - **GitHub リポジトリ URL**: 解析したい GitHub リポジトリの URL を入力します。
   - **ブランチ名**: 使用するブランチ名を入力します（デフォルトは `master`）。
   - **ファイル拡張子**: 解析したいファイルの拡張子をドロップダウンから選択します。選択肢にない場合は「その他」を選び、手動で拡張子を入力できます。
   - **クエリ**: 質問したい内容を入力します。

6. 「回答の出力」ボタンをクリックします。

7. 結果が表示されます。
