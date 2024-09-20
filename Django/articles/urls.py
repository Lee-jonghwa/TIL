
from django.urls import path

# 명시적 상대경로
from . import views

urlpatterns = [
    path('index/', views.index), # 함수는 호출은 안 되고, 주소만 들어감
    path('dinner/', views.dinner),# 새로운 페이지를 만들면 url을 새로 만들어야 함
    path('search/', views.search),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('hello/<str:name', views.greeting),
]


