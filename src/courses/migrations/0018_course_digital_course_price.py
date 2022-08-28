# Generated by Django 4.0.6 on 2022-08-28 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0017_alter_course_students'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='digital',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='price',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
