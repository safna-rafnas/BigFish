# Generated by Django 3.1.4 on 2020-12-28 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_auto_20201228_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products_db',
            name='image',
            field=models.ImageField(upload_to='productimage/'),
        ),
        migrations.AlterField(
            model_name='recipie_db',
            name='image',
            field=models.ImageField(upload_to='recipieimage/'),
        ),
    ]
