# Generated by Django 2.0.2 on 2018-02-21 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mussels_site', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='Program',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mussels_site.Program'),
        ),
    ]
