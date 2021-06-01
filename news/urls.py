from django.urls import path,
from news.views import home, category_item, region_item, contactform, TeamView

app_name = 'news'

urlpatterns = [
    path('', home, name='home'),
    path('news/category/<slug>', category_item, name='category-item'),
    path('region/<slug>', region_item, name='region-item'),
    path('contact/', contactform, name='contact'),
    path('our-team/', TeamView.as_view(), name='our-team'),



]