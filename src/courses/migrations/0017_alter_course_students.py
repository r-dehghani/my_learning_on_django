# Generated by Django 4.0.6 on 2022-08-25 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_alter_profile_profile_pic'),
        ('courses', '0016_course_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(blank=True, null=True, to='accounts.profile'),
        ),
    ]
