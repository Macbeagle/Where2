# Generated by Django 3.2.8 on 2021-10-25 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itinerary', '0007_auto_20211025_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='cost',
            field=models.CharField(choices=[('HI', 'High'), ('ME', 'Medium'), ('LO', 'Low')], max_length=2),
        ),
    ]
