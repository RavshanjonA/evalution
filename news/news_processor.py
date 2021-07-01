from news.models import Category, Region


def category_processor(request):
    data = {
        'categories': Category.objects.all().order_by('pk')
    }
    return data

def region_processor(request):
    data = {
        'regions': Region.objects.all().order_by('pk')
    }
    return data
