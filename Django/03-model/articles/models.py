from django.db import models

# Create your models here.
# 괄호 안은 상속할 클래스 -> models 모듈의 Model 클래스를 상속
class Article(models.Model):
    # 예를 들어 1번 게시글을 작성하면 id->1, title과 content는 각 작성한 내용들어감
    # 클래스로 title이라는 instance를 만듦
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)