import random
from django.shortcuts import render

# Create your views here.
def index(request): # 위치인자 1개는 필수

    # 템플릿에서 사용할 수 있도록 만드는 장치
    context = {
        'name' : 'alice',
    }


    # 메인 페이지를 응답
    return render(request, "articles/index.html", context)
    # render(요청 데이터, 템플릿 이름, 출력할 context)


def dinner(request):
    foods = ['국밥','국수','카레','탕수육',]
    picked = random.choice(foods)
    context = {
        'foods' : foods,
        # 'picked' : picked,
    }

    return render(request, 'articles/dinner.html', context)

def search(request):
    return render(request, 'articles/search.html')

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    message = request.GET.get('message')
    context = {
        'message' : message,
    }
    return render(request, 'articles/catch.html', context)


# variable routing의 순서대로 두 번째 이후에 인자를 작성함
def greeting(request, name):
    context = {
        'name' = name
    }
    return render(request, 'articles/greeting.html', context)