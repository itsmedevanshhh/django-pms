# Generated by Django 4.1.7 on 2023-04-09 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0014_rename_project_team_project_team_module'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project_task',
            name='task_util_minutes',
        ),
    ]