# Generated by Django 4.0.2 on 2022-02-12 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_question_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='city',
        ),
    ]
