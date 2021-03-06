# Generated by Django 3.2.1 on 2021-05-26 23:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Programs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_name', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProgramWithCourses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course1', models.CharField(default='', max_length=100)),
                ('course2', models.CharField(default='', max_length=100)),
                ('course3', models.CharField(default='', max_length=100)),
                ('course4', models.CharField(default='', max_length=100)),
                ('programs', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='myapp.programs')),
            ],
        ),
    ]
