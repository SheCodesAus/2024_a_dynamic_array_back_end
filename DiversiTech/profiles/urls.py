from django.urls import path
from . import views

urlpatterns = [
      path('profiles/', views.ProfileList.as_view()),
      path('profile/<int:pk>/', views.ProfileDetail.as_view()),
      path('industries/', views.IndustryList.as_view()),
      path('industries/<int:pk>', views.IndustryList.as_view()),
      path('tags/', views.TagList.as_view()),
      path('tag/<int:pk>/', views.TagList.as_view())
]