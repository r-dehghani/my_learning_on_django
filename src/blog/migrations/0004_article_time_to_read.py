# Generated by Django 4.0.6 on 2022-07-28 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_article_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='time_to_read',
            field=models.CharField(default='3 mins', max_length=50),
            preserve_default=False,
        ),
    ]
