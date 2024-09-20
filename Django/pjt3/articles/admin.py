from django.contrib import admin

# Register your models here.


# 현재 디렉토리의 models.py에서 Board라는 클래스를 가져옴
from .models import Board


# Board 모델을 Django 관리자 사이트에 등록
admin.site.register(Board)