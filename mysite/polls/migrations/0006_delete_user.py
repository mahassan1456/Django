# Generated by Django 4.0.2 on 2022-02-12 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
