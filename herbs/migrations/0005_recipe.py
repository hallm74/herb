# Generated by Django 5.1.4 on 2024-12-29 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herbs', '0004_alter_herbmedicinaluse_herb_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('text', models.TextField()),
                ('herbs', models.ManyToManyField(related_name='recipes', to='herbs.herb')),
            ],
        ),
    ]