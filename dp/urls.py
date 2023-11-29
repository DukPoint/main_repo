from django.urls import path
from . import views
from .views import MyPageView


urlpatterns = [
    path('store/', views.store),
    path('', views.main),
    path('mypage/', MyPageView.as_view(), name='mypage'),
]