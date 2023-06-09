# Generated by Django 4.1.7 on 2023-04-08 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0010_alter_projectmodule_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('COMPLETED', 'COMPLETED'), ('PENDING', 'PENDING'), ('CANCELLED', 'CANCELLED')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='status',
            name='status_name',
            field=models.CharField(choices=[('COMPLETED', 'COMPLETED'), ('PENDING', 'PENDING'), ('CANCELLED', 'CANCELLED')], max_length=100),
        ),
    ]
