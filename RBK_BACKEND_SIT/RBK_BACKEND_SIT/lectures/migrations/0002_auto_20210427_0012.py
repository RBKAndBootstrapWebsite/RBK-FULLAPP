# Generated by Django 3.1.3 on 2021-04-26 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lecture',
            old_name='content',
            new_name='title',
        ),
        migrations.AddField(
            model_name='lecture',
            name='url',
            field=models.TextField(default=''),
        ),
    ]
