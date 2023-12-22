# python:3.11の公式 image をベースの image として設定
FROM python:3.11

# 作業ディレクトリの作成
RUN mkdir /game_review

# 作業ディレクトリの設定（以後の RUN は WORKDIR で実行）
WORKDIR /game_review

# カレントディレクトリにある資産をコンテナ上の指定のディレクトリにコピーする
ADD web /game_review

# pipでrequirements.txtに指定されているパッケージを追加する
RUN pip install -r requirements.txt
