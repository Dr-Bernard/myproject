# Generated by Django 5.0.7 on 2024-07-28 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Doctors', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Doctors',
            new_name='Doctor',
        ),
    ]
