# Generated by Django 2.1.7 on 2019-03-26 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='trainer',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
