# Generated by Django 5.0.4 on 2024-05-04 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('profile_image', models.ImageField(upload_to='profile_images/')),
                ('address', models.CharField(max_length=255)),
            ],
        ),
    ]