# Generated by Django 2.1.5 on 2022-02-22 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20220221_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('entrees', 'entrees'), ('treats', 'treats'), ('drinks', 'drinks'), ('appetizers', 'appetizers')], max_length=60),
        ),
    ]