# Generated by Django 5.1.2 on 2024-10-14 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_apply_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='applied_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]