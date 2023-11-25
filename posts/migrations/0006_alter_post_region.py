# Generated by Django 3.2.23 on 2023-11-21 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_post_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='region',
            field=models.CharField(choices=[('Asia', 'Asia'), ('Africa', 'Africa'), ('North America', 'North America'), ('South America', 'South America'), ('Antarctica', 'Antarctica'), ('Europe', 'Europe'), ('Australien', 'Australien')], default='Europe', max_length=50),
        ),
    ]