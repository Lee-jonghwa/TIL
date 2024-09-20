from django.db import models

# Create your models here.


class Board(models.Model):
    # CharField의 필수 인자: max_length
    # 글자제한이 20자인 Field(column)
    title = models.CharField(max_length=20)
    # 글자제한이 없는 Text Field
    content = models.TextField()

    # DateField -> 날짜만
    # DateTimeField -> 날짜와 시간 모두

    # created -> 생성 시간
    # auto now add -> 객체가 처음 생성된 시간
    created_at = models.DateTimeField(auto_now_add=True)
    # updated -> 수정 시간
    # auto now -> 객체가 저장 될 때마다의 각 시간
    updated_at = models.DateTimeField(auto_now=True)

    xx_at = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.title # board에 title 표시