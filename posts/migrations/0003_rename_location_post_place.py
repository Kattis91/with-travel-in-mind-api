# Generated by Django 3.2.23 on 2023-11-15 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20231115_2219'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='location',
            new_name='place',
        ),
    ]
