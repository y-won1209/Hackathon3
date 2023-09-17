# Generated by Django 4.2 on 2023-08-17 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_alter_place_latitude_alter_place_longitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='latitude',
            field=models.DecimalField(decimal_places=10, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='longitude',
            field=models.DecimalField(decimal_places=10, max_digits=15, null=True),
        ),
    ]
