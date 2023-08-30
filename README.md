# MTG AI Assistant

## 概要

- 生成AIを利用し会議アシスタントツールです
- 文字起こしの生成、会議内容への質問が出来ます
- 詳しい内容はこちらの記事を参照ください
  - https://blog.cloudnative.co.jp/19749/

## 動作確認済の環境

- macOS 13.5
- Orbstack 0.16.0

## 構成図

![](https://blog.cloudnative.co.jp/wp-content/uploads/2023/08/mtg-ai-assistant-mtg-ai-assistant04-1920x921.png)

## セットアップ

- Orbstackをインストール
  - https://orbstack.dev/download
- Homebrewを利用していれば下記コマンドでインストール


```bash
brew install orbstack
```

## 起動方法

### Repoをclone

- 任意のディレクトリにclone
- ここでは `~/repos/` にcloneする例

```bash
mkdir ~/repos/
cd ~/repos/
git clone https://github.com/cloudnative-co/mtg-ai-assistant.git
cd mtg-ai-assistant
```

## .envファイルの作成

- OpenAI APIキーが必要のため取得
  - https://platform.openai.com/account/api-keys


```bash
cp .env.sample .env
```

エディタで `.env` を開いて編集。

```bash
OPENAI_API_KEY=sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```


### Orbstackを起動した状態で下記コマンドを実行

- 起動コマンドはMakefileにまとめてあるため下記でビルドと起動が出来ます

```bash
make build
make run
```


## 環境変数の扱い と .envrcの扱い

- 環境変数は`.env`ファイルに記載しています
- `.envrc` には記載しないでください
  - `.envrc` は `direnv` が利用するファイルで、`.env` を読み込む設定がしてあります

### .envrc の中身


```bash
dotenv
```
