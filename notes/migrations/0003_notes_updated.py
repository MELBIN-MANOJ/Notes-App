# Generated by Django 5.0.1 on 2024-08-04 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_notes_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
