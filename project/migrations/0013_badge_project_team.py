# Generated by Django 4.1.7 on 2023-04-09 08:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0012_project_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('badge', models.CharField(choices=[('InProgress', 'InProgress'), ('QuickFinisher', 'QuickFinisher'), ('LazyLoader', 'LazyLoader'), ('SilentUser', 'SilentUser')], max_length=25)),
            ],
            options={
                'db_table': 'badge',
            },
        ),
        migrations.CreateModel(
            name='Project_Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('Completed', 'Completed'), ('Pending', 'Pending'), ('Cancelled', 'Cancelled')], max_length=100)),
                ('badge', models.CharField(choices=[('IN', 'InProgress'), ('QF', 'QuickFinisher'), ('LL', 'LazyLoader'), ('SU', 'SilentUser')], max_length=25)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'project_team_module',
            },
        ),
    ]
