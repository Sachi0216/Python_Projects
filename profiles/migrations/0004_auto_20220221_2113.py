# Generated by Django 2.1.5 on 2022-02-22 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20220221_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(choices=[('Ms.', 'Ms.'), ('Mr.', 'Mr.'), ('Jr.', 'Jr'), ('Mrs.', 'Mrs.'), ('Sr.', 'Sr.')], max_length=30),
        ),
    ]