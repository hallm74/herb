# Generated by Django 5.1.4 on 2024-12-29 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herbs', '0005_recipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='herb',
            name='medicinal_uses',
            field=models.ManyToManyField(related_name='herbs', to='herbs.medicinaluse'),
        ),
    ]
