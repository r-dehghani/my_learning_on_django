# Generated by Django 4.0.6 on 2022-08-04 10:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_full_name', models.CharField(max_length=100, verbose_name='full name')),
                ('title', models.CharField(max_length=256)),
                ('user_email', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='email address')),
                ('location', models.CharField(blank=True, max_length=100, null=True, verbose_name='address')),
                ('about_me', models.TextField(blank=True, max_length=1000, null=True, verbose_name='a little about about your profile!')),
                ('profile_pic', models.ImageField(blank=True, upload_to='static/assets/images/profile_pictures')),
                ('telegram', models.URLField(blank=True, max_length=100, null=True, unique=True, verbose_name='telegram')),
                ('github', models.URLField(blank=True, max_length=100, null=True, unique=True, verbose_name='github')),
                ('linkedin', models.URLField(blank=True, max_length=100, null=True, unique=True, verbose_name='linkedin')),
                ('tweeter', models.URLField(blank=True, max_length=100, null=True, unique=True, verbose_name='tweeter')),
                ('instagram', models.URLField(blank=True, max_length=100, null=True, unique=True, verbose_name='instagram')),
                ('personal_website', models.URLField(blank=True, max_length=100, null=True, unique=True, verbose_name='personal website')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='MyUser',
        ),
    ]
