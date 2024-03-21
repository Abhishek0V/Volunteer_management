# Generated by Django 5.0.3 on 2024-03-21 00:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Volunteer', '0002_alter_volunteer_vol_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=60, null=True)),
                ('vol', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='volunter_model', to='Volunteer.volunteer')),
            ],
        ),
    ]