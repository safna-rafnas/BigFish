# Generated by Django 3.1.4 on 2021-02-14 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20210209_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='Total',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
