# Generated by Django 5.1.7 on 2025-03-28 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='contraseña',
            new_name='contrasena',
        ),
    ]
