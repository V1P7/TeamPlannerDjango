# Generated by Django 4.2.3 on 2023-08-07 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_user_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='vacations_days',
        ),
    ]
