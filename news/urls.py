from django.urls import path
from news.views import home, category_item, region_item, contactform, team_view, detail_view

app_name = 'news'

urlpatterns = [
    path('', home, name='home'),
    path('news/category/<slug>', category_item, name='category-item'),
    path('region/<slug>', region_item, name='region-item'),
    path('detail/<slug>', detail_view, name='detail-page'),
    path('contact/', contactform, name='contact'),
    path('our-team/', team_view, name='our-team'),
]