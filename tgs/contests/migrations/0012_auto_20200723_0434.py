# Generated by Django 3.0.6 on 2020-07-23 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0011_auto_20200723_0431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='djoin',
            name='whats_num',
            field=models.IntegerField(),
        ),
    ]
