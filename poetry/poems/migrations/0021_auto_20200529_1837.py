# Generated by Django 3.0.5 on 2020-05-29 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poems', '0020_remove_poem_custom_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poem',
            name='poet_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poems.Poet'),
        ),
    ]
