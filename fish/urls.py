from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='index'),
    path('fish.json', views.listFish),
    path('catch', views.changeCaught),
    path('auth/logout/', views.logout_view, name='logout'),
]
