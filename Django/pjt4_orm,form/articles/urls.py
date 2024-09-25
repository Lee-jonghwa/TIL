from django.urls import path

from . import views

app_name = 'articles'

urlpatterns = [
    # 홈페이지 -> 전체 게시글 조회
    path('', views.index, name='index'),
    # 단일 게시글 조회
    # variable routing --> 단순히 조회 목적
    # 1. views.py 함수에서 pk를 매개변수
    # 2. url naming pattern에서 article.pk 받아주기
    path('<int:pk>/', views.detail, name='detail'),
    
    # 생성
    # 페이지를 렌더링
    # path('new/',views.new, name='new'),
    # 페이지를 리다이렉트 => ModelForm을 통해 렌더링 + 리다이렉트로 통합
    path('create/', views.create, name='create'),   
    
    # 삭제 -> 조회 먼저 되기 때문에 단일 게시글에 대한 variable routing
    path('<int:pk>/delete/', views.delete, name='delete'),
    
    # 수정
    # 페이지 렌더링
    # path('<int:pk>/edit/', views.edit, name='edit'),
    # 페이지 리다이렉트 
    path('<int:pk>/update/', views.update, name='update'),
]
