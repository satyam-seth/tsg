# Generated by Django 3.0.6 on 2020-07-16 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='winner',
            name='team_logo',
            field=models.ImageField(default='Not Available', upload_to='home/'),
        ),
    ]
