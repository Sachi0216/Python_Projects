# Generated by Django 2.1.5 on 2022-02-22 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0015_profile_name'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='profile',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
        migrations.AddField(
            model_name='profile',
            name='title',
            field=models.CharField(choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Ms', 'Ms')], default='Mr', max_length=3),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Email',
            field=models.EmailField(blank=True, default='', max_length=90),
        ),
    ]
