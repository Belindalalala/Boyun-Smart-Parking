from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from . import models

class CarModelSerializers(ModelSerializer):
  
    class Meta:
        model = models.Car
        fields = '__all__'  # 或者明确列出需要的字段
        # 在 Meta 内部不需要定义 create() 方法

    def create(self, validated_data):
        # 自定义创建逻辑
        return models.Car.objects.create(**validated_data)