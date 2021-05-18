# Generated by Django 3.2.1 on 2021-05-16 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20210516_0058'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramWithCourses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_name', models.CharField(default='', max_length=100)),
                ('course1', models.CharField(default='', max_length=100)),
                ('course2', models.CharField(default='', max_length=100)),
                ('course3', models.CharField(default='', max_length=100)),
                ('course4', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='program',
            name='course',
        ),
    ]
