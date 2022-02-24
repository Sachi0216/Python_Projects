# Generated by Django 2.1.5 on 2022-02-22 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_auto_20220221_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='prefix',
            field=models.CharField(choices=[('Mr.', 'Mr.'), ('Sr.', 'Sr.'), ('Jr.', 'Jr.'), ('Mrs.', 'Mrs.'), ('Ms.', 'Ms.')], default='', max_length=6),
        ),
    ]