# Generated by Django 2.1.7 on 2019-03-26 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentCourse',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('course_id', models.CharField(max_length=10)),
            ],
        ),
    ]
