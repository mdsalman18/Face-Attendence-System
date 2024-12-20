# Generated by Django 5.0.7 on 2024-11-08 17:04

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CameraConfiguration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Give a name to this camera configuration', max_length=100, unique=True)),
                ('camera_source', models.CharField(help_text='Camera index (0 for default webcam or RTSP/HTTP URL for IP camera)', max_length=255)),
                ('threshold', models.FloatField(default=0.6, help_text='Face recognition confidence threshold')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('fname', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('phone_number', models.CharField(max_length=15)),
                ('rollno', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('batch', models.CharField(max_length=25)),
                ('phase', models.CharField(max_length=25)),
                ('image', models.ImageField(upload_to='students/')),
                ('authorized', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(editable=False, max_length=100)),
                ('Subject', models.CharField(editable=False, max_length=100)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('check_in_time', models.DateTimeField(blank=True, null=True)),
                ('check_out_time', models.DateTimeField(blank=True, null=True)),
                ('roll_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.student')),
            ],
        ),
    ]
