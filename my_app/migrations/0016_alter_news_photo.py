# Generated by Django 4.0.1 on 2022-09-16 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0015_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='photo',
            field=models.ImageField(upload_to='media/news'),
        ),
    ]
