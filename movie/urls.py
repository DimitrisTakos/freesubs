from django.urls import path
from movie import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.base, name='base'),
    path('', views.cheatsheet, name="cheatsheet"),
    path('download/<int:cheatsheet_id>/',
         views.download_cheatsheet, name='download_cheatsheet'),
    path('page2/', views.page2, name='page2'),
    path('page2/wildcards/', views.wildcards, name='wildcards'),
    path('page2/wildcards/season_1_wildcards/', views.season_1_wildcards, name='season_1_wildcards'),
    path('page2/movies2024/', views.movies2024, name='movies2024'),
    path('page2/thetattooist/', views.thetattooist, name='thetattooist'),
    path('page2/thewayhome/', views.thewayhome, name='thewayhome'),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)