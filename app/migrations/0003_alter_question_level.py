# Generated by Django 3.2.7 on 2021-09-11 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_question_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='level',
            field=models.CharField(choices=[(1, 'ONE'), (2, 'TWO'), (3, 'Three')], default=1, max_length=20),
        ),
    ]
