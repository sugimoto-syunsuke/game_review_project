#!/bin/sh
cd ./game_review
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

