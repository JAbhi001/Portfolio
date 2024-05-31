# Generated by Django 5.0.4 on 2024-05-28 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0010_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Service name')),
                ('description', models.TextField(verbose_name='About service')),
            ],
        ),
    ]
