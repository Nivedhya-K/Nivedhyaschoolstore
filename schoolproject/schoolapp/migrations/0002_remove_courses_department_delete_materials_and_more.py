# Generated by Django 5.0.1 on 2024-01-25 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='department',
        ),
        migrations.DeleteModel(
            name='Materials',
        ),
        migrations.DeleteModel(
            name='Courses',
        ),
        migrations.DeleteModel(
            name='Departments',
        ),
    ]
