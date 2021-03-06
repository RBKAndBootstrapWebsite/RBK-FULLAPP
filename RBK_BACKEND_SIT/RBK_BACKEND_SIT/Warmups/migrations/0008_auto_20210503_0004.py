# Generated by Django 3.1.3 on 2021-05-02 21:04

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('week', '0001_initial'),
        ('days', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cohort', '0001_initial'),
        ('Warmups', '0007_remove_warmups_title'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='warmups',
            unique_together={('student_name', 'cohort', 'week', 'day')},
        ),
    ]
