# Generated by Django 3.2.7 on 2021-09-12 03:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20210912_0315'),
    ]

    operations = [
        migrations.RenameField(
            model_name='point',
            old_name='attemp',
            new_name='attempt',
        ),
    ]