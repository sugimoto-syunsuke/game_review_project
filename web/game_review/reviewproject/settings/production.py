# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 11:34:35 2023

@author: sugimoto
"""

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# AWSで許可されてるホストを記入
ALLOWED_HOSTS = ['127.0.0.1','0.0.0.0','localhost']

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',   # sqliteから変更
        'NAME': 'game_review_db',     # プロジェクト用に作成したデータベース名
        'USER': os.environ['DATABASE_USER'],    # RDSで作成したユーザー名
        'PASSWORD': os.environ['DATABASE_PASSWORD'],    # RDSで作成したユーザーのパスワード
        'HOST': os.environ['DATABASE_HOST'],
        'PORT': os.environ['DATABASE_PORT'],
    }
}

# mediaフォルダーの場所(BASE_DIR以下のmedia)を登録
# S3を参照させる
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# アクセスキーID
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
# シークレットアクセスキー
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
# バケット名
AWS_STORAGE_BUCKET_NAME = 'game-review-django'
# 保存先URL
MEDIA_URL = 'https://%s.s3.ap-northeast-1.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
AWS_LOCATION = 'media'
