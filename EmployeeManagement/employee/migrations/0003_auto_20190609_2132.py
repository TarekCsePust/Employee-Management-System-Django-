# Generated by Django 2.1 on 2019-06-09 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20190609_2124'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='status',
            new_name='active',
        ),
    ]
