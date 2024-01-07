# django.views.generic から TemplateView、ListViewをインポート
from django.views.generic import TemplateView, ListView
# 写真投稿ページ作成に必要なクラス、モジュールをインポート
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import ReviewPostForm, GameForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# modelsモジュールからモデルReviewPostをインポート
from .models import Game, ReviewPost
# 詳細ページ用にDetailViewをインポート
from django.views.generic import DetailView
# 削除ページ用にDeleteViewをインポート
from django.views.generic import DeleteView
# 検索機能のために追加
from django.db.models import Q, Avg
from django.contrib import messages

class IndexView(ListView):
    '''
    トップページのビュー
    '''
    # index.htmlをレンダリングする
    template_name = 'index.html'
    # モデルBlogPostのオブジェクトにorder_by()を適用して
    # ゲーム名の降順で並び変える
    queryset = Game.objects.order_by('title')
    # 1ページに表示するレコードの件数
    paginate_by = 9
    
    def get_queryset(self):
        query = self.request.GET.get('query')
        queryset = Game.objects.order_by('title')
        if query:
            queryset = queryset.filter(
            Q(title__icontains=query)
            )
        messages.add_message(self.request, messages.INFO, query)
        return queryset
    
# デコレーターにより、CreateReviewViewへのアクセスはログインユーザーに限定される
# ログイン状態でなければsettings.pyのLOGIN_URLにリダイレクトされる
@method_decorator(login_required, name='dispatch')
class CreateReviewView(CreateView):
    '''レビュー投稿ページのビュー
    
    ReviewPostFormで定義されているモデルとフィールドと連携して
    投稿データをデータベースに登録する
    
    Attributes:
        form_class: モデルフィールドが登録されたフォームクラス
        template_name: レンダリングするテンプレート
        success_url: データベースへの登録完了後のリダイレクト先
    '''
    # forms.pyのReviewPostFormをフォームクラスとして登録
    form_class = ReviewPostForm
    # レンダリングするテンプレート
    template_name = "post_review.html"
    # データベースへの登録完了後のリダイレクト先
    success_url = reverse_lazy('review:post_done')
    
    def form_valid(self, form):
        '''CreateViewクラスのform_valid()をオーバーライド
        
        フォームのバリデーションを通過したときに呼ばれる
        フォームデータの登録をここで行う
        
        parameters:
            form(django.forms.Form):
                form_classに格納されているReviewPostFormオブジェクト
        Return:
            HttpResponseRedirectオブジェクト:
                スーパークラスのform_valid()の戻り値を返すことで、
                success_urlで設定されているURLにリダイレクトさせる
        '''
        # commit=FalseにしてPOSTされたデータを取得
        postdata = form.save(commit=False)
        # 投稿ユーザーのidを取得してモデルのuserフィールドに格納
        postdata.user = self.request.user
        # カスタムバリデーション
        if ReviewPost.objects.filter(user=postdata.user, game=self.request.POST.get('game', None)).exists() :
            form.add_error('game',  \
                '以前レビューしたゲームは再度レビューはできません。')
            return self.form_invalid(form)
        # 投稿データをデータベースに登録
        postdata.save()
        # 戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
        return super().form_valid(form)

class PostSuccessView(TemplateView):
    '''投稿完了ページのビュー
    
    Attributes:
        template_name: レンダリングするプレート
    '''
    # index.htmlをレンダリングする
    template_name = 'post_success.html'

class DetailView(DetailView):
    ''' 詳細ページのビュー
    投稿記事の詳細を表示するので、DetailViewを継承する
    
    Attributes:
        tempalte_name: レンダリングするテンプレート
        model: モデルのクラス
    '''
    # post.htmlをレンダリングする
    template_name = 'detail.html'
    # クラス変数modelにモデルを設定
    model = Game
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['review_list'] = ReviewPost.objects.filter(game=self.kwargs['pk'])
        context['average_score'] = context['review_list'].aggregate(Avg('score'))['score__avg']
        context['myreview_is'] = False
        # TODO 未ログイン時にmyreviewの部分を読み込むとエラーになるので、やむなく二重for文を使用
        # フィルターでuserに未ログイン時のユーザにIDが無いのが原因の可能性有
        if self.request.user.is_authenticated:
            myreview = ReviewPost.objects.filter(user=self.request.user, game=self.kwargs['pk'])
            if myreview.exists():
                context['myreview_is'] = True
                context['myreview_id'] = myreview.get().pk
        return context

class MypageView(ListView):
    ''' マイページのビュー
    
    Attributes:
        tempalte_name: レンダリングするテンプレート
        paginate_by: 1ページに表示するレコードの件数
    '''
    # index.htmlをレンダリングする
    template_name = 'mypage.html'
    # ゲーム名の降順で並び変える
    queryset = Game.objects.order_by('title')
    # 1ページに表示するレコードの件数
    paginate_by = 9
    
    def get_queryset(self):
        # ReviewPostからログインユーザがレビューしたことのあるゲームを抽出
        my_game = ReviewPost.objects.filter(
            user=self.request.user).order_by('-posted_at').values_list('game', flat=True)
        queryset = Game.objects.filter(pk__in=my_game)
        return queryset

class ReviewDeleteView(DeleteView):
    ''' レコード削除ビュー
    Attributes:
        tempalte_name: レンダリングするテンプレート
        model: モデルのクラス
        paginate_by: 1ページに表示するレコードの件数
        success_url: データベースへの登録完了後のリダイレクト先
    '''
    # 操作の対象はReviewPostモデル
    model = ReviewPost
    # review_delete.htmlをレンダリングする
    template_name = 'review_delete.html'
    # 処理完了後にマイページにリダイレクト
    success_url = reverse_lazy('review:mypage')
    
    def delete(self, request, *args, **kwargs):
        '''レコードの削除を行う
        
        Parameters:
            self: ReviewDeleteViewオブジェクト
            request: WSGIRequest(HttpRequest)オブジェクト
            args: 引数として渡される辞書(dict)
            kwargs: キーワード付きの辞書(dict) {'pk': 21}のようにレコードのidが表示される
        
        Returns:
            HttpResponseRedirect(success_url)を返して
            success_urlにリダイレクト
        '''
        # スーパークラスのdelete()を実行
        return super().delete(request, *args, **kwargs)

@method_decorator(login_required, name='dispatch')
class CreateGameView(CreateView):
    '''ゲーム追加ページのビュー
    
    GameFormで定義されているモデルとフィールドと連携して
    投稿データをデータベースに登録する
    
    Attributes:
        form_class: モデルフィールドが登録されたフォームクラス
        template_name: レンダリングするテンプレート
        success_url: データベースへの登録完了後のリダイレクト先
    '''
    # forms.pyのGameFormをフォームクラスとして登録
    form_class = GameForm
    # レンダリングするテンプレート
    template_name = "post_game.html"
    # データベースへの登録完了後のリダイレクト先
    success_url = reverse_lazy('review:post_game_done')
    
    def form_valid(self, form):
        '''CreateViewクラスのform_valid()をオーバーライド
        
        フォームのバリデーションを通過したときに呼ばれる
        フォームデータの登録をここで行う
        
        parameters:
            form(django.forms.Form):
                form_classに格納されているReviewPostFormオブジェクト
        Return:
            HttpResponseRedirectオブジェクト:
                スーパークラスのform_valid()の戻り値を返すことで、
                success_urlで設定されているURLにリダイレクトさせる
        '''
        # commit=FalseにしてPOSTされたデータを取得
        postdata = form.save(commit=False)
        # 投稿データをデータベースに登録
        postdata.save()
        # 戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
        return super().form_valid(form)

class PostGameSuccessView(TemplateView):
    '''投稿完了ページのビュー
    
    Attributes:
        template_name: レンダリングするプレート
    '''
    # index.htmlをレンダリングする
    template_name = 'post_game_success.html'