# Generated by Django 3.2.7 on 2021-09-12 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_question_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='attemp',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='level',
            field=models.CharField(choices=[('1', 'ONE'), ('2', 'TWO'), ('3', 'Three')], default='1', max_length=20),
        ),
    ]
