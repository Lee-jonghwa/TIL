from django.contrib import admin
from django.urls import path

# . -> 현재 디렉토리
from . import views

# 아무거나 상관 없으나 헷갈릴 수 있 기 때문에 이름 통일
#{% url 'articles:index' %} 와 같은 형식에서 articles가 app_name, 뒤에 나오는 index는 view 함수가 아님

app_name = "articles"

# name = 'index' ==> naming url pattern
# href = "/index/"와 같이 직접 적어야할 수고를 덜어줌(name으로 참조)
urlpatterns = [
    # articles/index/가 됨
    path('index/', views.index, name='index'),

    path('dinner/', views.dinner, name='dinner'),
    
    path('search/', views.search, name='search'),
    
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),

    # <데이터타입:변수명> => 여러 개의 중복된 URL을 하나의 view로 처리하기 위함
    path('<int:number>', views.detail, name="detail"),
]
