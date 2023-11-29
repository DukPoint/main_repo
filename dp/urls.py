from django.urls import path
from . import views
from .views import search

urlpatterns = [
    path('store/', views.store),
    path('', views.main),
    path('search/', search, name='search'),
]