# Generated by Django 3.1 on 2020-08-27 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0002_auto_20200827_1555'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserRegistrForm',
            new_name='User',
        ),
    ]
