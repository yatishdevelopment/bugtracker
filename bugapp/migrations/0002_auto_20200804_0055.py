# Generated by Django 3.0.8 on 2020-08-03 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_type',
            field=models.CharField(max_length=100),
        ),
    ]