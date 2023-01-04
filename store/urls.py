from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('signup/', views.Signup.as_view(), name="signup"),
    path('login/', views.Login.as_view(), name="login"),
]
