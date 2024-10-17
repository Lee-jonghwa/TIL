from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer

@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        # 전체 게시글 조회
        # 타입: 쿼리셋 -> django에서 사용하는 형식
        articles = Article.objects.all()
        # 변환하기 쉬운 포맷으로 전환 (직렬화)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        # 사용자로부터 데이터를 입력받아 직렬화 진행
        serializer = ArticleSerializer(data=request.data)
        # 유효성 검사
        if serializer.is_valid(raise_exception=True): # DRF에서 동일하게 만든 것
            serializer.save()
            # 저장 성공 후 201 응답 코드 반환
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # 유효성 실패 후 400 응답 코드 반환
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','DELETE','PUT'])
def article_detail(request, article_pk):
        # 단일 게시글 조회
    article = Article.objects.get(pk=article_pk)
    if request.method == 'GET':
        # 직렬화
        serializer = ArticleSerializer(article) # QuerySet을 반환하지 않으므로 many 필요없음
        return Response(serializer.data)
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = ArticleSerializer(data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)