# Generated by Django 5.0.4 on 2024-05-28 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutme',
            name='contact',
            field=models.IntegerField(),
        ),
    ]