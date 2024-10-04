from django.shortcuts import render

# Create your views here.
def index(request):
  # movies = Movie.objects.all()
  # context = {
  #   "movies" : movies,
  # }
  return render(request, 'movies/index.html')

# 유효성 검사
def create(request):
  pass