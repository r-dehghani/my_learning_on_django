# Generated by Django 4.0.6 on 2022-07-21 03:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='my_User',
        ),
    ]