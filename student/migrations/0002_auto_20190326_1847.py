# Generated by Django 2.1.7 on 2019-03-26 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentcourse',
            name='course_id',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='studentcourse',
            name='id',
            field=models.CharField(max_length=25, primary_key=True, serialize=False),
        ),
    ]
