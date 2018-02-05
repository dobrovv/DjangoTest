from django.urls import path

from . import views

urlpatterns = [
    path('user/register', views.UserRegisterView.as_view()),
    path('user/login', views.UserLoginView.as_view()),
    path('user/logout', views. UserLogoutView.as_view()),
    path('user/me', views.UserMeView.as_view()),
    path('user/', views.UserView.as_view()),

]
