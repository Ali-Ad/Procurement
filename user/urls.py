from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('register/', views.register),
    path('logout/', views.CustomerLogout.as_view(), name='logout'),
    path('change_password/', views.ChangePasswordView.as_view(), name='change_pass'),
    path('lock/',views.Lock.as_view()),
]
