# Generated by Django 5.0.1 on 2024-01-16 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0002_owner_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='phone_number',
        ),
    ]
