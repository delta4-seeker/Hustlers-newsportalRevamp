# Generated by Django 3.0.7 on 2022-12-13 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='writer',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
