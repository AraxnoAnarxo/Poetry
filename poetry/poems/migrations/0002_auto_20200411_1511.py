# Generated by Django 3.0.4 on 2020-04-11 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poems', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='poem',
            old_name='tag',
            new_name='poem_tag',
        ),
    ]
