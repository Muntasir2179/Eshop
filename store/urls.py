from django.urls import path
from . import views
from .middleware import auth_middleware

urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    path('signup/', views.Signup.as_view(), name="signup"),
    path('login/', views.Login.as_view(), name="login"),
    path('logout/', views.logout, name="logout"),
    path('cart/', views.Cart.as_view(), name="cart"),
    path('check_out/', auth_middleware(views.CheckOut.as_view()), name="check_out"),
    path('orders/', auth_middleware(views.Orders.as_view()), name="orders"),
]
