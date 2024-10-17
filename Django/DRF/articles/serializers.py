from rest_framework import serializers 
from .models import Article, Comment

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # 직렬화 하고자 하는 필드를 지정
        fields = ('id', 'title', 'content',)

class ArticleSerializer(serializers.ModelSerializer):
    # 게시글에 해당하는 댓글
    # CommentDetailSerializer는 반드시 ArticleSerializer에서만 사용되기 때문
    class CommentDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ('id','content',)
    # 필드 2개 추가 -> 읽기 전용 필드(read_only=True) 설정
    # 읽기 전용 필드 사용하는 경우
    # 1. 사용자로부터 입력 받지 않는다.
    # 2. 유효성 검사 과정에서 제외된다.
    # 3. 결과 데이터가 클라이언트에 제공된다.
    comment_set = CommentDetailSerializer(many=True, read_only=True)
    
    comment_count = serializers.IntegerField(
        # comment_set : 역참조 매니저, count: 메서드
        source = 'comment_set.count', read_only=True
    )
    class Meta:
        model = Article
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    # 댓글을 조회했을 때, 게시글의 제목도 같이 나오게
    class ArticleTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title',)
    # 댓글을 조회했을 때 같이 나오는 게시글의 제목은 읽기 전용
    article = ArticleTitleSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
            