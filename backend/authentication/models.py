from django.db import models

class Manege(models.Model):
    username = models.CharField(max_length=100)
    password = models.TextField()

    class Meta:
        db_table = 'manage'
