# Generated by Django 3.2.1 on 2021-05-20 00:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_programwithcourses_program_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='programwithcourses',
            name='program_name',
        ),
        migrations.AddField(
            model_name='programwithcourses',
            name='programs',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='myapp.programs'),
        ),
    ]
