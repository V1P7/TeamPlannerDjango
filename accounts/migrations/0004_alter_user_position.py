# Generated by Django 4.2.3 on 2023-07-29 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_birthday_alter_user_join_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='position',
            field=models.CharField(max_length=20),
        ),
    ]
