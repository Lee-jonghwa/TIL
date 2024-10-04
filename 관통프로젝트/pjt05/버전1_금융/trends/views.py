from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
from selenium import webdriver
import requests

from .models import Trend, Keyword
from .forms import TrendForm, KeywordForm

import re

def extract_number(result_text):
    match = re.search(r'[\d,]+', result_text)
    
    if match:
        # 쉼표가 포함된 문자열을 숫자로 변환
        number_str = match.group().replace(',', '')  # 쉼표 제거
        return int(number_str)  # 정수형으로 변환
    return None

def search_keyword(keyword):
    url = f"https://www.google.com/search?q={keyword}"
    driver = webdriver.Chrome()
    driver.get(url)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    result_stats = soup.select_one("div#result-stats")

    driver.quit()

    if result_stats:
        return extract_number(result_stats.text)
    else:
        return '검색 결과를 찾을 수 없습니다.'

def keyword(request): ## 메인페이지
    queries = Keyword.objects.all()

    if request.method == 'POST':
        form = KeywordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trends:keyword')
    else:
        form = KeywordForm()
        context = {
        'queries': queries,
        'form':form,
    }
    return render(request, 'trends/keyword.html', context)

def keyword_detail(request, pk): ## 삭제
    del_keyword = Keyword.objects.get(pk=pk)
    if request.method == 'POST':
        del_keyword.delete()
        return redirect('trends:keyword')

# Create your views here.

    
def crawling(request): # 크롤링 하는 거
    # 사용자가 검색을 하면 크롤링을 진행
    keywords = Keyword.objects.all()

    # 웹 페이지 요청 및 크롤링
    try:
        for keyword in keywords:
            search_result = search_keyword(keyword.name)
            # Trend 테이블 업데이트 또는 생성
            trend, created = Trend.objects.get_or_create(name=keyword.name,search_period='all', result=search_result, created_at=keyword.created_at)
            if not created:
                trend.result= search_result
                trend.search_period = 'all'
                trend.save()
    except requests.exceptions.RequestException as e:
        context = {
            'page_title': '크롤링 에러',
            'error_message': str(e)
        }
        return render(request, 'trends/crawling.html', context)
    
    keywords = Keyword.objects.all()
    trends = Trend.objects.filter(name__in=keywords)
    context = {
        'keywords': keywords,
        'trends': trends,
    }
    return render(request, 'trends/crawling.html', context)

def crawling_histogram(request):
    context ={

    }
    return render(request, 'trends/crawling_histogram.html', context)

def crawling_advanced(request):
    context = {
        
    }
    return render(request, 'trends/crawling_advanced.html', context)