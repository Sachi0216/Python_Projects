# Generated by Django 2.1.5 on 2022-02-22 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20220221_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('treats', 'treats'), ('drinks', 'drinks'), ('entrees', 'entrees'), ('appetizers', 'appetizers')], max_length=60),
        ),
    ]