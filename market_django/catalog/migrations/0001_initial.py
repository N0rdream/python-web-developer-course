# Generated by Django 2.0.2 on 2018-02-13 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'attributes',
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'brands',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50)),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Attribute')),
            ],
            options={
                'db_table': 'features',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to='')),
            ],
            options={
                'db_table': 'images',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Category')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Image')),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='ProductData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Feature')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Product')),
            ],
            options={
                'db_table': 'product_data',
            },
        ),
    ]
