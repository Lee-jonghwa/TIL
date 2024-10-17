from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            'id',
            'title',
            'content',
        )


class ArticleSerializer(serializers.ModelSerializer):
    class CommentDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ('id', 'content',)

    comment_set = CommentDetailSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    class Meta:
        model = Article
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class ArticleTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title',)
    # 기존 article 데이터 값을 override
    # 기존 필드를 override하게 되면 read_only_fields를 사용할 수 없음
    # => read_only 인자값 사용
    article = ArticleTitleSerializer(read_only=True)

    class Meta:
        models = Comment
        # fields에 작성된 필드는 모두 유효성 검사 목록에 포함됨
        fields = '__all__'
        # 외래키 필드를 읽기 전용 필드로 지정
        # => 유효성 검사에서는 제외하고 결과에는 포함
        # read_only_fields = ('article',)