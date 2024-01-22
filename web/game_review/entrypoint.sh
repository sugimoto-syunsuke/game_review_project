#!/bin/sh
cd ./game_review
# 開発と本番で読み込む設定ファイルを出し分ける
if [ $1 = 0 ]
then
       export DJANGO_SETTINGS_MODULE=reviewproject.settings.production
else
       export DJANGO_SETTINGS_MODULE=reviewproject.settings.develop
fi
python manage.py makemigrations accounts review
python manage.py migrate --noinput
python manage.py collectstatic --noinput
# 第一引数が1(開発環境)の時はrunserverを、0(本番環境)の時はgunicornを実行
if [ $1 = 0 ]
then
	# gunicornを起動させる時はプロジェクト名を指定
	gunicorn reviewproject.wsgi:application --bind 0.0.0.0:8000
else
	python manage.py runserver 0.0.0.0:8000
fi

