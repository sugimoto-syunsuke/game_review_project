from django.contrib import admin
# CustomUserをインポート
from .models import Game, ReviewPost

class GameAdmin(admin.ModelAdmin):
    '''管理ページのレコード一覧に表示するカラムを設定するクラス
    '''
    # レコード一覧にidとtitleを表示
    list_display = ('id', 'title')
    # 表示するカラムにリンクを設定
    list_display_links = ('id', 'title')

class ReviewPostAdmin(admin.ModelAdmin):
    '''管理ページのレコード一覧に表示するカラムを設定するクラス
    '''
    # レコード一覧にidとtitleを表示
    list_display = ('id', 'title')
    # 表示するカラムにリンクを設定
    list_display_links = ('id', 'title')

# Django管理サイトにCategory,CategoryAdminを登録する
admin.site.register(Game, GameAdmin)

# Django管理サイトにReviewPost,ReviewPostAdminを登録する
admin.site.register(ReviewPost, ReviewPostAdmin)