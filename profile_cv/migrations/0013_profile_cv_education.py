# Generated by Django 3.1.2 on 2020-10-01 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_cv', '0012_auto_20201001_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile_cv',
            name='education',
            field=models.ManyToManyField(related_name='my_education', to='profile_cv.Education'),
        ),
    ]