# Generated by Django 5.1.4 on 2024-12-28 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('herbs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='herb',
            name='image',
        ),
    ]