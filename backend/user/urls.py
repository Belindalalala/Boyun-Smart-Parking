from django import urls
from django.urls import path
from .views import UserList, UserDetail, sample

urlpatterns = [
  path('users/', UserList.as_view(), name="user-list"),
  path('users/<int:pk>/', UserDetail.as_view(), name="user-detail"),
  path('sample', sample, name="sample")
]