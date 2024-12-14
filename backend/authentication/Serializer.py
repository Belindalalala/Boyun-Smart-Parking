from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from . import models

class ManageModelSerializers(ModelSerializer):
    username = serializers.CharField(read_only=True)

    class Meta:
        model = models.Manege
        fields = '__all__'
