from django.urls import path
from . import views
from .views import SignInView, SignUpView, SignUpView2
from .views import main
from .views import logout


urlpatterns = [
    path('logout/', views.logout, name='logout'),
    path('store/', views.store),
    path('', views.main, name='main'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signup2/', SignUpView2.as_view(), name='signup2'),
    path('signin/', SignInView.as_view(), name='signin'),
]

