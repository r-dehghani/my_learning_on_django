# Generated by Django 4.0.6 on 2022-08-04 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_alter_myuser_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='about_me',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='a little about about your profile!'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='github',
            field=models.URLField(blank=True, max_length=100, null=True, unique=True, verbose_name='github'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='instagram',
            field=models.URLField(blank=True, max_length=100, null=True, unique=True, verbose_name='instagram'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='linkedin',
            field=models.URLField(blank=True, max_length=100, null=True, unique=True, verbose_name='linkedin'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='personal_website',
            field=models.URLField(blank=True, max_length=100, null=True, unique=True, verbose_name='personal website'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='telegram',
            field=models.URLField(blank=True, max_length=100, null=True, unique=True, verbose_name='telegram'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='tweeter',
            field=models.URLField(blank=True, max_length=100, null=True, unique=True, verbose_name='tweeter'),
        ),
    ]
