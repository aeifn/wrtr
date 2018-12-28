from django.shortcuts import render, redirect
from core.models import Article
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def article(request, id):
    article = Article.objects.get(id=id)
    text = article.text
    return HttpResponse(text, content_type="text/plain")

def add(request):
    if request.method == "POST":
        text = request.POST.get('text')
        article = Article()
        article.text = text
        article.save()
        return redirect('article', article.id)
         
    if request.method == "GET":
        return render(request, 'add.html')
