# Generated by Django 2.0.2 on 2018-02-19 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20180219_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='file',
            field=models.ImageField(upload_to=''),
        ),
    ]
