# Generated by Django 2.1.5 on 2022-02-24 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0030_auto_20220224_0127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('drinks', 'drinks'), ('treats', 'treats'), ('entrees', 'entrees'), ('appetizers', 'appetizers')], max_length=60),
        ),
    ]