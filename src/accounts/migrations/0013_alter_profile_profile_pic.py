# Generated by Django 4.0.6 on 2022-08-07 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='static/assets/images/profile_pictures'),
        ),
    ]
