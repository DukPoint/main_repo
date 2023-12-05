from django.urls import path
from . import views
from .views import MyPageView
from .views import search
from .views import SignInView, SignUpView, SignUpView2, SignUpView3, SignUpView4, SignUpView5
from .views import main
from .views import logout

urlpatterns = [
    path('order_payment/<int:store_id>/<int:menu_id>/', views.OrderPayment.as_view(), name='order_payment'),
    path('store_menu/<int:pk>/', views.StoreMenu.as_view(), name='store_menu'),
    path('logout/', views.logout, name='logout'),
    path('store/', views.store, name='store'),
    path('mypage/', MyPageView.as_view(), name='mypage'),
    path('search/', search, name='search'),
    path('', views.main, name='main'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signup2/', SignUpView2.as_view(), name='signup2'),
    path('signup3/', SignUpView3.as_view(), name='signup3'),
    path('signup4/', SignUpView4.as_view(), name='signup4'),
    path('signup_complete/', SignUpView5.as_view(), name='signup_complete'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('review1/', views.review1, name='review1'),
]

