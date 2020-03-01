from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import  static

urlpatterns=[
    path('',views.index, name = 'indexPage'),
    path('',views.search_results, name='search_results'),
    path('', views.filter_by_location, name='location'),
    path('',views.filter_by_category, name='category'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL_ROOT)

