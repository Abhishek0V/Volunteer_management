# Generated by Django 5.0 on 2024-03-21 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0005_registered_volunteers'),
    ]

    operations = [
        migrations.AddField(
            model_name='registered_volunteers',
            name='Selected',
            field=models.BooleanField(default=False),
        ),
    ]
