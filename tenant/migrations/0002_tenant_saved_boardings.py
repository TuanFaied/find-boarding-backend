# Generated by Django 5.0.1 on 2024-01-16 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boarding', '0004_boardinghouse_phone_number'),
        ('tenant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenant',
            name='saved_boardings',
            field=models.ManyToManyField(blank=True, related_name='tenants', to='boarding.boardinghouse'),
        ),
    ]
