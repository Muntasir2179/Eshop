from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    path('signup/', views.Signup.as_view(), name="signup"),
    path('login/', views.Login.as_view(), name="login"),
    path('logout/', views.logout, name="logout"),
    path('cart/', views.Cart.as_view(), name="cart"),
]
