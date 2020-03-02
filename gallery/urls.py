from django.urls import path,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import  static

urlpatterns=[
    path('',views.index, name = 'indexPage'),
    path('search/',views.search_results, name='search_results'),
    path('catrgory/',views.search_location, name='category'),
    re_path('images/(\d+)/',views.search_image, name='images'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

