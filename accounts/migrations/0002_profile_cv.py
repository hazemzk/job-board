# Generated by Django 5.1.2 on 2024-10-19 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cv',
            field=models.FileField(default=1, upload_to='profile/'),
            preserve_default=False,
        ),
    ]