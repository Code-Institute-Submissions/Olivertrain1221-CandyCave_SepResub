# Generated by Django 3.2 on 2022-06-24 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sweets', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Sweets',
            new_name='Sweet',
        ),
    ]