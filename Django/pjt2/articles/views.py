from django.shortcuts import render
import random

# Create your views here.

def index(request):
    # context는 딕셔너리 구조
    # templates에서 {{ name }}과 같이 활용 시 key의 value값을 활용할 수 있음
    context = {
        'name' : 'Jane',
        'number' : 1,
    }

    # 항상 render 함수의 3번째 인자는 context
    return render(request, 'articles/index.html', context)

def dinner(request):
    foods = ['족발', '보쌈', '치킨', '피자']
    picked = random.choice(foods)
    context = {
        'foods' : foods,
        'picked' : picked,
    }

    return render(request, 'articles/dinner.html', context)


def search(request):
    return render(request, 'articles/search.html')


def throw(request):
    return render(request, 'articles/throw.html')


# throw로 보낸 건 이미 request에 들어있음
def catch(request):
    text = request.GET.get('throw')

    context = {
        'talk' : text,
    }

    return render(request, 'articles/catch.html', context)


def detail(request, number):
    # urls.py에서 정의한 변수가 아닌 변수를 받으면 오류 뜸
    context = {
        'num' : number
    }

    return render(request, 'articles/detail.html', context)