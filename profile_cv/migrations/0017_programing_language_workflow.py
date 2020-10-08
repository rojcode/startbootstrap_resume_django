# Generated by Django 3.1.2 on 2020-10-02 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_cv', '0016_auto_20201002_0955'),
    ]

    operations = [
        migrations.CreateModel(
            name='Programing_Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Programing language',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='WorkFlow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workflow', models.CharField(max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
