# Generated by Django 5.0.1 on 2024-01-16 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boarding', '0003_alter_boardinghouse_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='boardinghouse',
            name='phone_number',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
