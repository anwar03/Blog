# Generated by Django 2.0.3 on 2018-03-21 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0001_initial'),
        ('article', '0007_auto_20180314_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(to='tag.Tag'),
        ),
    ]
