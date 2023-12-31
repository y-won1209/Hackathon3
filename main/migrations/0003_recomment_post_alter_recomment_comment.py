# Generated by Django 4.2 on 2023-08-12 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_post_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='recomment',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='main.post'),
        ),
        migrations.AlterField(
            model_name='recomment',
            name='comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recomments', to='main.comment'),
        ),
    ]
