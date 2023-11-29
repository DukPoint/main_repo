from django.urls import path
from . import views
from .views import SignInView, SignUpView, SignUpView2

urlpatterns = [
    path('store/', views.store),
    path('', views.main),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signup2/', SignUpView2.as_view(), name='signup2'),
    path('signin/', SignInView.as_view(), name='signin'),
]

