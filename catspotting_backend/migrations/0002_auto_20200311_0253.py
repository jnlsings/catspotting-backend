# Generated by Django 3.0.4 on 2020-03-11 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catspotting_backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.CharField(max_length=1000),
        ),
    ]
