# Generated by Django 2.1.7 on 2019-03-27 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0006_auto_20190326_1847'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('timestamp', models.DateTimeField(auto_now_add=True, primary_key=True, serialize=False)),
                ('content_name', models.CharField(max_length=100)),
                ('content_file', models.FileField(default='', upload_to='')),
                ('course_id', models.CharField(max_length=100)),
            ],
        ),
    ]
