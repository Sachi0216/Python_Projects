# Generated by Django 2.1.5 on 2022-02-22 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(blank=True, default='', max_length=30)),
                ('Email', models.CharField(blank=True, default='', max_length=90)),
                ('Username', models.CharField(max_length=90)),
            ],
        ),
    ]
