# Generated by Django 2.2.6 on 2019-11-06 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20191106_1023'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='label',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='name',
            new_name='label',
        ),
    ]
