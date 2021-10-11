from django.urls import path
from . import views

urlpatterns = [
    path('login', views.LoginView.as_view(), name = 'sign-in'),
    path('logout', views.logout_view, name = 'sign-out'),
]
