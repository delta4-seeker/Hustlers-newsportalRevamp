# Generated by Django 3.0.7 on 2022-12-17 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_auto_20221213_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='audio',
            field=models.ImageField(default=0, upload_to='images/'),
            preserve_default=False,
        ),
    ]