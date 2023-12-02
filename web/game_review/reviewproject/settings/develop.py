# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 11:34:19 2023

@author: sugimoto
"""

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# mediaフォルダーの場所(BASE_DIR以下のmedia)を登録
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# mediaのURLを登録
MEDIA_URL = '/media/'