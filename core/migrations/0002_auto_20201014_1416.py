# Generated by Django 3.1.2 on 2020-10-14 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='imdb_title_id',
            field=models.CharField(max_length=20),
        ),
    ]
