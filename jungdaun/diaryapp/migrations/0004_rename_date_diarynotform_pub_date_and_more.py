# Generated by Django 4.2.1 on 2023-06-27 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diaryapp', '0003_alter_diarynotform_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diarynotform',
            old_name='date',
            new_name='pub_date',
        ),
        migrations.AlterField(
            model_name='diarynotform',
            name='weather',
            field=models.CharField(max_length=20),
        ),
    ]