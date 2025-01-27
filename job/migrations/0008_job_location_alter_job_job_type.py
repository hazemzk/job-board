# Generated by Django 5.1.2 on 2024-10-15 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_apply_applied_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='location',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('Full time', 'Full time'), ('Part time', 'Part time')], max_length=15),
        ),
    ]
