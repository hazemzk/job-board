# Generated by Django 5.1.2 on 2024-10-20 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_profile_cv_profile_specialization'),
        ('job', '0016_alter_job_job_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='specialization',
        ),
        migrations.AddField(
            model_name='profile',
            name='specialization',
            field=models.ManyToManyField(to='job.category'),
        ),
    ]