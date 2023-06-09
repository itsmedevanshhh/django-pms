# Generated by Django 4.1.7 on 2023-04-09 07:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0011_alter_project_status_alter_status_status_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project_Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_title', models.CharField(max_length=100)),
                ('task_description', models.TextField()),
                ('priority', models.CharField(choices=[('High', 'High Priority'), ('Less', 'Less Priority')], max_length=30)),
                ('task_estimated_hours', models.IntegerField()),
                ('task_util_minutes', models.IntegerField()),
                ('status', models.CharField(choices=[('Completed', 'Completed'), ('Pending', 'Pending'), ('Cancelled', 'Cancelled')], max_length=100)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.projectmodule')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'project_task',
            },
        ),
    ]
