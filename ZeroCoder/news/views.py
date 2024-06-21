from django.shortcuts import render
from .models import News_post

def news_home(request):
    news = News_post.objects.all()
    return render(request, 'news/news.html', {'news': news})