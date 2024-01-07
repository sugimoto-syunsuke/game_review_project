# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 21:52:06 2023

@author: ABEBE
"""

from django.urls import path
from . import views

# URLパターンを逆引き出来るように名前をつける = 'review'
app_name = 'review'

# URLパターンを登録する変数
urlpatterns = [
   # reviewアプリへのアクセスはviewsモジュールのIndexViewを実行
   path('', views.IndexView.as_view(), name='index'),
   
   # 写真投稿ページへのアクセスはviewsモジュールのCreateReviewViewを実行
   path('post/', views.CreateReviewView.as_view(), name='post'),
   
   # 投稿完了ページへのアクセスはviewsモジュールのCreateReviewViewを実行
   path('post_done/',
        views.PostSuccessView.as_view(),
        name='post_done'),
   
   # 詳細ページ
   # review-detail/<Review postsテーブルのid値>にマッチング
   # <int:pk>は辞書{pk: id値(int)}としてDetailViewに渡される
   path('review-detail/<int:pk>',
        views.DetailView.as_view(),
        name = 'review_detail'
        ),
   
   # マイページへのアクセスはviewsモジュールのMypageViewを実行
   path('mypage/',
        views.MypageView.as_view(),
        name='mypage'),
   
   # 投稿レビューの削除
   # reviews/<Review postsテーブルのid値>にマッチング
   # <int:pk>は辞書{pk: id値(int) }としてDetailViewに渡される
   path('review/<int:pk>/delete',
        views.ReviewDeleteView.as_view(),
        name = 'review_delete'
        ),
   
   # ゲーム追加ページ
   path('post_game/', views.CreateGameView.as_view(), name='post_game'),
   
   # ゲーム追加完了ページ
   path('post_game_done/',
        views.PostSuccessView.as_view(),
        name='post_game_done'),
]