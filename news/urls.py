from django.urls import path

from news.views import home

app_name = 'news'

urlpatterns = [
    path('', home, name='home'),
]
