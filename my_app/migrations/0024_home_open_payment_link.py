# Generated by Django 4.0.1 on 2022-09-20 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0023_catagory_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='open_payment_link',
            field=models.BooleanField(default=False),
        ),
    ]
