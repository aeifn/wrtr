from django.shortcuts import render, redirect
from core.models import Article

# Create your views here.
def index(request):
    return render(request, 'index.html')

def article(request, id):
    article = Article.objects.get(id=id)
    context = {
        'title': article.title,
        'text': article.text,
        }
    return render(request, 'article.html', context)

def add(request):
    if request.method == "POST":
        title = request.POST.get('title')
        text = request.POST.get('text')
        article = Article()
        article.title = title
        article.text = text
        article.save()
        return redirect('article', article.id)
         
    if request.method == "GET":
        return render(request, 'add.html')
