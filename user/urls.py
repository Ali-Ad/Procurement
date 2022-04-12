from django.urls import path
from .views import *
urlpatterns = [
    path('lll/',CustomLoginView.as_view()),

]