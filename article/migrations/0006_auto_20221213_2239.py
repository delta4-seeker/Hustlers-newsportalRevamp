# Generated by Django 3.0.7 on 2022-12-13 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20221213_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecategory',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='readerinterest',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]