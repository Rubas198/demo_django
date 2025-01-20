from django.http import HttpResponse
from django.shortcuts import render



def home(request):
    return render(request,'index.html')

def downloaded_files(request):
    return HttpResponse('<h1>dose not have any downloaded files at the moment')

def ingredients_list(request):
    return HttpResponse('<h1>Ingredients will be displayed here for the specific recipe')

def result(request):

    return render(request,'result.html')

def text(request):
    article = request.GET.get('article', 'default_value')

    return render(request,'text.html',{article:article})

