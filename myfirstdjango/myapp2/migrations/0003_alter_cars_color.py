# Generated by Django 4.1 on 2022-08-27 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0002_cars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='color',
            field=models.CharField(max_length=200, verbose_name='Color'),
        ),
    ]
