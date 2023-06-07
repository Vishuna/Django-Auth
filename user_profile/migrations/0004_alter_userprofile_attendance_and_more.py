# Generated by Django 4.2.1 on 2023-06-05 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0003_alter_userprofile_attendance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='attendance',
            field=models.CharField(choices=[('present', 'present'), ('absent', 'absent'), ('leave', 'leave')], max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=10),
        ),
    ]