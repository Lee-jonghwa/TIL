from django.shortcuts import render, redirect

from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    # QuerySet API => 전체 데이터 조회: Article.objects.all()
    articles = Article.objects.all()
    context = {
        'articles':articles
    }
    return render(request,'articles/index.html', context)

# 단일 게시글 페이지 렌더링
def detail(request,pk):
    # QuerySet API -> 단일 데이터 조회
    # 단일 게시글 조회이기 때문에 articles가 아닌 article
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }

    return render(request,'articles/detail.html', context)

# ModelForm 사용해서
def create(request):
    # 게시글 생성 버튼을 눌렀을 때
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        # 유효성 검사 대표 케이스
        # 1. 모든 필수 필드가 채워짐 여부
        # 2. 입력된 데이터가 필드의 조건(ex: 데이터 형식)을 만족하는지
        if form.is_valid():
            article = form.save()
            # create 함수 부분
            return redirect('articles:detail', article.pk)
    # 생성 버튼 누르기 전 또는 다른 버튼 눌렀을 때
    else:
        # 이제 채워야하기 때문에 값이 비워짐
        form = ArticleForm()
    # 1. 유효성 검사 통과하지 못한 경우 -> 제출했던 내용을 그대로 유지하기 위해 context에 form을 넣어줌
    # 2. GET 요청인 경우 -> new.html에 접속한 경우

    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)

"""
def new(request):
    return render(request, 'articles/new.html')


# render와 redirect 차이
# render -> 사용자에게 새로운 페이지를 보여줄 때 사용
# redirect -> 데이터가 변경되었을 때 경로에 요청

def create(request):
    # create 방법 중 2번 방법 사용 / 3번은 절대 x
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 코드가 간결하고 save를 나중에 하므로 안정성이 있음
    article = Article(title=title, content=content)
    article.save()
    
    # 게시글 생성 후 어떤 페이지로 이동할 지
    # 클라이언트가 GET 요청을 한 번 더 보내도록 함
    # redirect(urlnaming, 요소)
    return redirect('articles:detail', article.pk)
""" 

def delete(request, pk):
    # 조회
    article = Article.objects.get(pk=pk)
    # 삭제
    article.delete()
    # 페이지를 돌아가기
    return redirect('articles:index')


def update(request,pk):
    # 조회 먼저 하기
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        # 기존 게시글의 데이터를 미리 채우기
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    # 변경 버튼 누르기 전 또는 다른 버튼 눌렀을 때
    else:
        form = ArticleForm(instance=article)
    context = {
        # 기존에 받았던 정보
        'article':article,
        'form':form,
    }
    return render(request, 'articles/update.html', context)

"""
# 사용자 데이터 입력 받기
def edit(request, pk):
    # 조회 -> 기존에 있는 게시글
    article = Article.objects.get(pk=pk)
    context = {
        'article':article,
    }
    return render(request, 'articles/edit.html', context)

# 입력받은 데이터 DB 반영
def update(request, pk):
    # 조회 -> 기존에 있는 게시글
    article = Article.objects.get(pk=pk)
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 바꾸기
    article.title = title
    article.content = content
    
    # 저장
    article.save()

    return redirect('articles:detail', article.pk)
"""