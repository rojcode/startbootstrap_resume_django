# Generated by Django 3.1.2 on 2020-10-01 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_cv', '0008_auto_20201001_1848'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile_cv',
            name='color_hex',
        ),
        migrations.DeleteModel(
            name='Theme_Profile',
        ),
    ]