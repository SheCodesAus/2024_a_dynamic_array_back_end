from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.CustomUserList.as_view()),
    path('users/<str:username>/', views.CustomUserDetail.as_view()),
]
