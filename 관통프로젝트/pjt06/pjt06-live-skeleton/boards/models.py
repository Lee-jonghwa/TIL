from django.db import models
from django.conf import settings


# Create your models here.
class Board(models.Model): 
    # 실제로는 유저 탈퇴 시 DB에서 잘 안 날림
    author = models.ForeignKey(settings.User, on_delete=models.DO_NOTHING, related_name='boards')
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
