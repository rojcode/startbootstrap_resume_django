# Generated by Django 3.1.2 on 2020-10-01 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profile_cv', '0007_auto_20201001_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile_cv',
            name='color_hex',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='my_hex_color', to='profile_cv.theme_profile'),
        ),
        migrations.AlterField(
            model_name='theme_profile',
            name='hex_color',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
    ]