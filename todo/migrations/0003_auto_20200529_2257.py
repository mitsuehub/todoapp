# Generated by Django 3.0.6 on 2020-05-29 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_done'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Done',
            new_name='DoneTable',
        ),
    ]
