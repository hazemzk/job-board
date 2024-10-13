# Generated by Django 5.1.2 on 2024-10-13 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.AlterField(
            model_name='job',
            name='experience',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('Part time', 'Part time'), ('Full time', 'Full time')], max_length=15),
        ),
    ]
