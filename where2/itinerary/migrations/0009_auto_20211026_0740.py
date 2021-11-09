# Generated by Django 3.2.8 on 2021-10-25 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itinerary', '0008_alter_activity_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='cost',
            field=models.CharField(choices=[('HI', 'High'), ('ME', 'Medium'), ('LO', 'Low'), ('FR', 'Free')], max_length=2),
        ),
        migrations.AlterField(
            model_name='food',
            name='cost',
            field=models.CharField(choices=[('HI', 'High'), ('ME', 'Medium'), ('LO', 'Low'), ('FR', 'Free')], max_length=2),
        ),
        migrations.DeleteModel(
            name='Itinerary',
        ),
    ]
