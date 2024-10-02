from django.contrib.auth.forms import UserCreationForm, UserChangeForm


# 직접 참조
# from .models import User

# 간접 참조
# get_user_model()이 커스텀 User모델을 자동으로 변환해줌
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # model = User ==> 직접 참조
        model = get_user_model()


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        # 회원정보 변경할 필드 설정
        # ==> migrations의 0001 파일에서 확인 가능(또는 DB)
        fields = ('first_name','last_name','email',)