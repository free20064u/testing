# Generated by Django 3.2.1 on 2021-06-03 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('phone_number', models.CharField(blank=True, default='', max_length=200)),
                ('email', models.EmailField(max_length=100)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_student', models.BooleanField(default=False)),
                ('password', models.CharField(max_length=100)),
                ('passwordConfirm', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='programs',
            options={'ordering': ['program_name']},
        ),
        migrations.AlterModelOptions(
            name='programwithcourses',
            options={'ordering': ['programs']},
        ),
        migrations.AlterField(
            model_name='programwithcourses',
            name='programs',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.programs'),
        ),
    ]
