# Generated by Django 3.2.7 on 2021-09-12 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_point_passed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='level',
        ),
    ]