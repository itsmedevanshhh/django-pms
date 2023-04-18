# Generated by Django 4.1.7 on 2023-04-05 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_rename_tatus_project_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectmodule',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Pending', 'Pending'), ('Cancelled', 'Cancelled')], max_length=100),
        ),
    ]