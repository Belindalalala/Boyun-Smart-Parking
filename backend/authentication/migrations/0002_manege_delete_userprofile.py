# Generated by Django 4.2.14 on 2024-12-14 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manege',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
