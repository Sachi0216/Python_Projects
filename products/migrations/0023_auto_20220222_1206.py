# Generated by Django 2.1.5 on 2022-02-22 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0022_auto_20220222_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('entrees', 'entrees'), ('treats', 'treats'), ('appetizers', 'appetizers'), ('drinks', 'drinks')], max_length=60),
        ),
    ]