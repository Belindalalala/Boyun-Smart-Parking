from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from rest_framework import generics
from .models import User
from .serializer import UserModelSerializers

class UserList(generics.ListCreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserModelSerializers

  def post(self, request, *args, **kwargs):
    return super().post(request, *args, **kwargs)
  
  def get(self, request, *args, **kwargs):
    return super().get(request, *args, **kwargs)
  
  def perform_create(self, serializer):
    serializer.save()


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = User.objects.all()
  serializer_class = UserModelSerializers

  def get(self, request, *args, **kwargs):
    return super().get(request, *args, **kwargs)
  
  def put(self, request, *args, **kwargs):
    return super().put(request, *args, **kwargs)
  
  def delete(self, request, *args, **kwargs):
    return super().delete(request, *args, **kwargs)
  
  def perform_update(self, serializer):
    serializer.save()

  def perform_destroy(self, instance):
    instance.delete()

def sample(HttpRequest):
  return HttpResponse("Hello World! from backend")
