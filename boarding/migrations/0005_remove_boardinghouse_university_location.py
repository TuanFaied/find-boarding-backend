# Generated by Django 5.0.1 on 2024-01-18 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boarding', '0004_boardinghouse_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boardinghouse',
            name='university_location',
        ),
    ]
