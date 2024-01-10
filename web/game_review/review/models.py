from django.db import models
from accounts.models import CustomUser
from django.core.validators import MaxValueValidator, MinValueValidator

class Game(models.Model):
    '''投稿するレビューのゲーム情報を管理するモデル
    '''
    title = models.CharField(
        verbose_name='ゲーム名', #フィールドのタイトル
        max_length=20)
    
    # イメージのフィールド１
    image1 = models.ImageField(
        verbose_name='ゲーム画像', # フィールドのタイトル
        upload_to = 'reviews' # MEDIA_ROOT以下のreviewsにファイルを保存
        )
    
    def __str__(self):
        '''オブジェクトを文字列に変換して返す
        Returns(str):カテゴリ名
        '''
        return self.title

class ReviewPost(models.Model):
    '''投稿されたデータを管理するモデル
    '''
    # CustomUserモデル(のuser_id)とReviewPostモデルを
    # 1対多の関係で結びつける
    # CustomUserが親でReviewPostが子の関係になる
    user = models.ForeignKey(
        CustomUser,
        # フィールドのタイトル
        verbose_name='ユーザー',
        # ユーザーを削除する場合はそのユーザの投稿データも全て削除する)
        on_delete=models.CASCADE
        )
    # Gameモデル(のtitle)とReviewPostモデルを
    # 1対多の関係で結びつける
    # Gameが親でReviewPostが子の関係になる
    game = models.ForeignKey(
        Game,
        # フィールドのタイトル
        verbose_name='ゲーム名',
        # ゲーム名に関連つけられた投稿データが存在する場合は
        # そのゲーム情報を削除出来ないようにする
        on_delete=models.PROTECT
        )
    # タイトル用のフィールド
    title = models.CharField(
        verbose_name='レビューのタイトル', # フィールドのタイトル
        max_length=50 # 最大文字数は50
        )
    # コメント用のフィールド
    comment = models.TextField(
        verbose_name='レビュー本文', # フィールドのタイトル
        max_length=2000 # 最大文字数は2000
        )
    # 点数用のフィールド
    score = models.IntegerField(
        verbose_name='点数', # フィールドのタイトル
        validators=[MinValueValidator(0), MaxValueValidator(100)] # 0から100の整数
        )
    # 投稿日時のフィールド
    posted_at = models.DateTimeField(
        verbose_name='投稿日時', # フィールドのタイトル
        auto_now_add=True # 日時を自動追加
        )
    
    def __str__(self):
        '''オブジェクトを文字列に変換して返す
        Returns(str):投稿記事のタイトル
        '''
        return self.title