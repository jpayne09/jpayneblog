# Generated by Django 3.0.6 on 2020-05-25 23:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0002_entry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='data_added',
            new_name='date_added',
        ),
    ]
