# Generated by Django 4.0.1 on 2022-09-17 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0019_user_is_payment_apcepted'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='media/projects'),
        ),
    ]
