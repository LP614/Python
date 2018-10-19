from django.shortcuts import render

# Create your views here.
from app.models import Article


def index(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        return render(request, 'index.html', {'articles': articles})


def info(request,id):
    if request.method == 'GET':
        article = Article.objects.filter(pk=id).first()
        return render(request, 'info.html', {'article': article})






