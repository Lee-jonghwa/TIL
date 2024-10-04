from django.urls import path
from . import views

app_name = 'weathers'

urlpatterns = [
    path('problem1/', views.problem1, name = 'problem1'),
]
