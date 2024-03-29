# Generated by Django 4.0.1 on 2022-09-20 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0021_alter_project_leader'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inaguration_crermony_chief_guest', models.BooleanField(default=False)),
                ('closing_crermony_chief_guest', models.BooleanField(default=False)),
                ('honorable_judge', models.BooleanField(default=False)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='media/Guest')),
                ('name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('facebook_link', models.URLField(blank=True, null=True)),
                ('Twiter_link', models.URLField(blank=True, null=True)),
                ('Linkedin_link', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
