# UserCreationFormクラスをインポート
from django.contrib.auth.forms import UserCreationForm
# models.pyで定義したカスタムUserモデルをインポート
from .models import CustomUser
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
    '''UsrCreationFormのサブクラス'''
    class Meta:
        '''UserCreationFormのインナークラス
        Attributes:
            model:連携するUserモデル
            fields:フォームで使用するフィールド
        '''
        # 連携するUserモデルを設定
        model = CustomUser
        # フォームで使用するフィールドを設定
        # ユーザ名、メールアドレス、パスワード、パスワード（確認用）
        fields = ('username', 'email', 'password1', 'password2')
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if not email:
            raise ValidationError(
                _("メールアドレスを入力してください"),
                code="null-email"
            )
        if not '@' in email:
            raise ValidationError(
                _("メールアドレスに@が含まれていません"),
                code="not-@-email"
            )
        return email
    