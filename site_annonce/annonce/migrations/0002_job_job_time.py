# Generated by Django 5.0.6 on 2024-05-14 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annonce', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_time',
            field=models.CharField(blank=True, choices=[('TN', 'Temps Plein'), ('TP', 'Temps Partiel')], max_length=2),
        ),
    ]
