from django import urls
from django.urls import path
from .views import CarList, CarDetail, sample

urlpatterns = [
  path('cars/', CarList.as_view(), name="car-list"),
  path('cars/<int:pk>/', CarDetail.as_view(), name="car-detail"),
  path('sample', sample, name="sample")
]