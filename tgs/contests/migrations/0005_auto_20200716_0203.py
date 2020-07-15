# Generated by Django 3.0.6 on 2020-07-16 02:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0004_auto_20200716_0156'),
    ]

    operations = [
        migrations.RenameField(
            model_name='daily',
            old_name='d_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='daily',
            old_name='d_fees',
            new_name='fees',
        ),
        migrations.RenameField(
            model_name='daily',
            old_name='d_type',
            new_name='match_type',
        ),
        migrations.RenameField(
            model_name='daily',
            old_name='d_tgames',
            new_name='total_games',
        ),
        migrations.RenameField(
            model_name='monthly',
            old_name='m_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='monthly',
            old_name='m_fees',
            new_name='fees',
        ),
        migrations.RenameField(
            model_name='monthly',
            old_name='m_type',
            new_name='match_type',
        ),
        migrations.RenameField(
            model_name='monthly',
            old_name='m_tgames',
            new_name='total_games',
        ),
        migrations.RenameField(
            model_name='weekly',
            old_name='w_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='weekly',
            old_name='w_fees',
            new_name='fees',
        ),
        migrations.RenameField(
            model_name='weekly',
            old_name='w_type',
            new_name='match_type',
        ),
        migrations.RenameField(
            model_name='weekly',
            old_name='w_tgames',
            new_name='total_games',
        ),
    ]
