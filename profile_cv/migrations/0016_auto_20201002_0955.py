# Generated by Django 3.1.2 on 2020-10-02 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_cv', '0015_education_time_line'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='degree',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
