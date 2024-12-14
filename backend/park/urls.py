from django import urls
from django.urls import path
from .views import ParkList, ParkDetail, sample

urlpatterns = [
  path('parks/', ParkList.as_view(), name="park-list"),
  path('parks/<int:pk>/', ParkDetail.as_view(), name="park-detail"),
  path('sample', sample, name="sample")
]