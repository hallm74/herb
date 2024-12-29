# Generated by Django 5.1.4 on 2024-12-29 00:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herbs', '0003_alter_herbmedicinaluse_herb_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='herbmedicinaluse',
            name='herb',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='herb_medicinal_uses', to='herbs.herb'),
        ),
        migrations.AlterField(
            model_name='herbmedicinaluse',
            name='medicinal_use',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medicinal_use_herbs', to='herbs.medicinaluse'),
        ),
    ]
