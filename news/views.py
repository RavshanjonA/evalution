from django.http import HttpResponse
from django.shortcuts import render, redirect

from news.forms import MessageForm
from news.models import Category, Region, Employee, Article


def home(request):
    article = Article.objects.all().order_by('-published_at')
    data = {
        'posts': article,
    }

    return render(request, 'news/home.html', context=data)


def category_item(request, slug):
    article = Article.objects.filter(category__slug=slug).order_by('-published_at')
    data = {
        'posts': article,
    }
    return render(request, 'news/category.html', context=data)


def region_item(request, slug):
    article = Article.objects.filter(region__slug=slug).order_by('-published_at')
    data = {
        'posts': article,
    }
    return render(request, 'news/region.html', context=data)


def contactform(request):
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            print("Success")
            return redirect('news:home')
    categories = Category.objects.all().order_by('pk')
    data = {
        'categories': categories,
        'form': form
    }
    return render(request, 'news/message.html', data)


def detail_view(request, slug):
    ariticle = Article.objects.get(slug=slug)
    data = {'post':ariticle}
    return render(request, 'news/detail.html',data )


def team_view(request):
    employees = Employee.objects.all()

    data = {
        'employees': employees,
    }

    return render(request, 'news/team.html', context=data)
