from django.contrib import admin
from django.urls import path
from . import views

app_name = "pages"

# name = 'index' ==> naming url pattern
# href = "/index/"와 같이 직접 적어야할 수고를 덜어줌(name으로 참조)
urlpatterns = [
    path('index/',views.index, name='index'),
]
