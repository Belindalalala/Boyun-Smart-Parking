from django.db import models

# Car model
class Car(models.Model):
    id = models.AutoField(primary_key=True)
    owner_name  = models.CharField(max_length=255)
    license_plate  = models.CharField(max_length=255)


    class Meta:
        db_table = 'car'
