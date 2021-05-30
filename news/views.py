from django.http import HttpResponse
from django.shortcuts import render

from news.forms import MessageForm
from news.models import Category, Region


def home(request):
    categories = Category.objects.all().order_by('pk')
    regions = Region.objects.all().order_by('pk')
    data = {
        'categories': categories,
        'regions': regions,
    }
    return render(request, 'news/home.html', context=data)
def category_item(request,slug):
    category = Category.objects.get(slug=slug)
    return HttpResponse(f'<h3> This slug is {slug} belong to {category.name}</h3>')

def region_item(request,slug):
    region = Region.objects.get(slug=slug)
    return HttpResponse(f'<h3>This slug is {slug} belong to {region.name}</h3>')

def contactform(request):
    form = MessageForm()
    if request.method == 'post':
        if form.is_valid:
            print("Success")
    return render(request,'news/message.html',context={'form':form})
