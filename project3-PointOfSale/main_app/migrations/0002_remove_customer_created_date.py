# Generated by Django 4.1.5 on 2023-01-09 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='created_date',
        ),
    ]