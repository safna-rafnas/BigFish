# Generated by Django 3.1.4 on 2021-02-28 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_remove_cart_cmail'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='userid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='webapp.regdb'),
        ),
    ]