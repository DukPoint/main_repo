from django.urls import path
from . import views

urlpatterns = [
    path('store/', views.store),
    path('mypage/', views.mypage, name='mypage'),
    path('', views.main),
]