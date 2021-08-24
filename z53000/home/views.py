from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from .models import News
from .serializers import NewsJson
from .forms import NewNew
import time


def home(request):  # request - obaviazkova
    data = News.objects.filter(category__name='Famali')
    return render(request, 'home/home_page.html', {"data": data})


def news(request):
    data = News.objects.filter(category__name='News')
    return render(request, 'home/news.html', {"data": data})


def my_api(request):
    data_from_db = News.objects.all()
    some_data = NewsJson(data_from_db, many=True)
    return JsonResponse(some_data.data, safe=False)


def add_new(request):
    if request.method == 'POST':
        form = NewNew(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/news/')
    return render(request, 'home/add_news.html', {'form': NewNew()})


