from django.forms import ModelForm, ModelChoiceField
from .models import ReviewPost, Game

class CustomModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj): # label_from_instance 関数をオーバーライド
         return obj.title # 表示したいカラム名を return

class ReviewPostForm(ModelForm):
    '''ModelFormのサブクラス
    '''
    game = CustomModelChoiceField(queryset=Game.objects.all())
    class Meta:
        '''ModelFormのインナークラス
        Attributes:
            model: モデルのクラス
            fields: フォームで使用するモデルのフィールドを作成
        '''
        model = ReviewPost
        fields = ['game', 'title', 'comment', 'score']