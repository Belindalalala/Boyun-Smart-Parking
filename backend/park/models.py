from django.db import models

# Park model
class Park(models.Model):
    id = models.AutoField(primary_key=True)
    license_plate  = models.CharField(max_length=255)
    parking_area = models.CharField(max_length=255)
    parking_number = models.CharField(max_length=255)
    entry_time = models.DateTimeField()
    exit_time = models.DateTimeField()
    fee = models.FloatField()

    class Meta:
        db_table = 'record'
