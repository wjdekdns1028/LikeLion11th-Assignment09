# Generated by Django 4.2.2 on 2023-06-21 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journalapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journaluseform',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]