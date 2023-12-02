# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 11:34:35 2023

@author: sugimoto
"""

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# AWSで許可されてるホストを記入
ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',   # sqliteから変更
        'NAME': 'djangodb',     # プロジェクト用に作成したデータベース名
        'USER': os.environ['DATABASE_USER'],    # RDSで作成したユーザー名
        'PASSWORD': os.environ['DATABASE_PASSWORD'],    # RDSで作成したユーザーのパスワード
        'HOST': os.environ['DATABASE_HOST'],
        'PORT': os.environ['DATABASE_PORT'],
    }
}

# mediaフォルダーの場所(BASE_DIR以下のmedia)を登録
# TODO S3から読み込めるようにしたい
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# mediaのURLを登録
MEDIA_URL = '/media/'