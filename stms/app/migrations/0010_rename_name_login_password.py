# Generated by Django 4.1.4 on 2023-02-25 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_login'),
    ]

    operations = [
        migrations.RenameField(
            model_name='login',
            old_name='name',
            new_name='password',
        ),
    ]
