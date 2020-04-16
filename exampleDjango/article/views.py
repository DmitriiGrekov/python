from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

def index(request):
    articles = Article.objects.all()
    return render(request,'article/main.html',{'ar':articles})

def show_one(request,pk):
    article = Article.objects.get(pk = pk)


    return render(request,'article/show_one.html',{'ar':article
        })




# Create your views here.
