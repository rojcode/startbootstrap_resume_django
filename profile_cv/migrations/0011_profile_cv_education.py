# Generated by Django 3.1.2 on 2020-10-01 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_cv', '0010_education'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile_cv',
            name='education',
            field=models.ManyToManyField(blank=True, related_name='my_education', to='profile_cv.Education'),
        ),
    ]
