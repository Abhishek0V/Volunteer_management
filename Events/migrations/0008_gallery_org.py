# Generated by Django 5.0.3 on 2024-03-25 02:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0007_gallery'),
        ('Org', '0004_org_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='org',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='org_profile', to='Org.org'),
        ),
    ]
