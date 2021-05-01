from django.http import HttpResponse
from django.shortcuts import render

from news.models import Category, Region


def home(request):
    categories = Category.objects.all().order_by('pk')
    regions = Region.objects.all().order_by('pk')
    data = {
        'categories': categories,
        'regions': regions,
    }
    return render(request, 'news/base.html', context=data)
