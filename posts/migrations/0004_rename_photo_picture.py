# Generated by Django 4.0.4 on 2022-05-15 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_photo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Photo',
            new_name='Picture',
        ),
    ]
