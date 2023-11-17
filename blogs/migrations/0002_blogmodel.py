# Generated by Django 4.1.7 on 2023-11-17 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(default='', max_length=100)),
                ('title', models.CharField(default='', max_length=100)),
                ('message', models.CharField(default='', max_length=100)),
            ],
        ),
    ]