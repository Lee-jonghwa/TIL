from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
import base64
from io import BytesIO
plt.switch_backend('Agg')

csv_path = 'weathers/data/austin_weather.csv'
# Create your views here.

# 간단히 페이지 렌더링
def problem1(request):
  df = pd.read_csv(csv_path)
  context = {
    'df' : df
  }
  return render(request, 'weathers/problem1.html', context)
