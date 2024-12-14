from django.db import models
from enum import Enum

# 定义一个枚举类
class UserStatus(Enum):
    HOTEL_STAFF = 'HOTEL_STAFF'
    VIP = 'VIP'
    SVIP = 'SVIP'
    GUEST = 'GUEST'
    VISITOR = 'VISITOR'

    def __str__(self):
        return self.value

# User model
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    status = models.CharField(
        max_length=200,  # 设置为枚举最大值的长度
        choices=[(tag.name, tag.value) for tag in UserStatus],  # 枚举值的选择
        default=UserStatus.VISITOR.name  # 默认值
    )

    class Meta:
        db_table = 'user'
