# Generated by Django 3.0.4 on 2020-05-01 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PoetsForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poet_checkbox', models.BooleanField(default=False, verbose_name='Лермонтов')),
            ],
        ),
    ]
