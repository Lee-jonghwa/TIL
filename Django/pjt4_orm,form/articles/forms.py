from django import forms
from .models import Article


# ModelForm 쓰면서 생각해야할 부분
# form 태그와, django ModelForm 차이
# 사용자로부터 입력받은 데이터를 DB에 저장하는지 안 하는지?
# form 태그 사용해도 DB에 저장 가능, 단 수동으로 구현해야 함.
# 상황에 따라 form과 ModelForm을 사용해야할 때가 있음(예: 풀스택 개발 시 등)
# ModelForm을 왜 쓸까? 편하고 길이가 짧음, 효율성이 좋음 + 유효성 검사 용이

class ArticleForm(forms.ModelForm):
    # 모델폼의 설계 구조라고 생각하기
    # class Meta -> 폼의 기본 구조를 자동으로 생성 --> 세부 조정 가능(Field, exclude, widgets 등)
    class Meta:
        model = Article
        # fields = ('title','content', 'created_at', 'updated_at')
        fields = "__all__"
        # updated_at을 빼려면 exclude = 'updated_at'