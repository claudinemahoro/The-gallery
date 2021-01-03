from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.welcome,name = 'welcome'),
    url(r'^search/',  views.search_results,name='search_results'),
    url(r'^location/(\d+)',  views.filter_by_location,name='location'),
    url(r'^image/(\d+)',  views.image,name='image')
]