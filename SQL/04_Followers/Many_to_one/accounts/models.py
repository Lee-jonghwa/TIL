from django.db import models
# Create your models here.
# AbstractUser : 로그인, 권한 관리 등에 필요한 기본적인 필드 제공
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  followings = models.ManyToManyField(
    # 대칭일 때 symmetrical -> False
    'self', symmetrical=False, related_name='followers'
  )
