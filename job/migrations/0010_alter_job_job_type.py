# Generated by Django 5.1.2 on 2024-10-15 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0009_job_owner_alter_job_job_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('Full time', 'Full time'), ('Part time', 'Part time')], max_length=15),
        ),
    ]
