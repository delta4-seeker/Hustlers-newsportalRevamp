# Generated by Django 3.0.7 on 2022-12-13 01:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='ArticleCategory',
        ),
    ]