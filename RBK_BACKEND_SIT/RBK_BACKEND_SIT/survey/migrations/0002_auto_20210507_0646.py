# Generated by Django 3.1.3 on 2021-05-07 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cohort', '0002_auto_20210505_0217'),
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey',
            name='status',
        ),
        migrations.AddField(
            model_name='survey',
            name='cohort',
            field=models.ManyToManyField(to='cohort.Cohort'),
        ),
    ]