# Generated by Django 2.1.7 on 2019-03-27 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20190326_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentcourse',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]