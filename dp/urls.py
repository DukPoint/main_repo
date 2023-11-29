from django.urls import path
from . import views
from .views import main
from .views import logout


urlpatterns = [
    path('store/', views.store),
    path('', views.main),
    path('main/', main, name='main'),
    path('logout/', logout, name='logout'),
]
