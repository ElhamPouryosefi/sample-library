# Generated by Django 4.1.5 on 2023-01-03 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newlibrary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]