# Generated by Django 2.2.17 on 2020-11-25 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheets', '0006_auto_20201121_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlibrary',
            name='sheets',
            field=models.ManyToManyField(to='sheets.Sheet'),
        ),
    ]
