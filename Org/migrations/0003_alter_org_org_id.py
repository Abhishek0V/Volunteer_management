# Generated by Django 5.0.3 on 2024-03-19 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Org', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='org',
            name='Org_ID',
            field=models.BigAutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]