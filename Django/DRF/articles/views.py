from django.shortcuts import render, get_list_or_404, get_object_or_404
# 4xx : 클라이언트 에러
# 5xx : 서버 에러
# 404 : Not Found, 잘못 입력

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Article, Comment
from .serializers import (
    ArticleListSerializer,
    ArticleSerializer,
    CommentSerializer
)

# Create your views here.
# GET : 게시글 조회
# POST : 게시글 생성
# DELETE : 게시글 삭제
# PUT : 게시글 수정
@api_view(['GET','POST'])
def article_list(request):
    if request.method == 'GET':
        # articles = Article.objects.all()
        articles = get_list_or_404(Article)
        # 모든 게시글을 DB에서 가져오고 -> 직렬화(json데이터 만들기 위함)
        # many=True -> 다중데이터(여러개의 객체)일 때 사용
        serializer = ArticleListSerializer(articles, many=True)
        # 직렬화된 데이터를 json 형식으로 응답한다.
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer, status=status.HTTP_201_CREATED)
        ## raise_exception=True 이므로 유효성 검사에 유효하지 않을 경우 자동 처리
        # return Response(serializer, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET': # 단일 게시글 조회
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'DELETE': # 단일 게시글 삭제
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT': # 단일 게시글 수정
        serializer =ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        # return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def comment_list(request):
    # 댓글이 하나도 없을 때 404 에러
    comments = get_list_or_404(Comment)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['POST'])
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)