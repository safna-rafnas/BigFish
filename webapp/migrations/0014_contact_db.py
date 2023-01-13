# Generated by Django 4.1.5 on 2023-01-05 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0013_remove_cart_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_db',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=10)),
                ('subject', models.CharField(max_length=20)),
                ('message', models.TextField(max_length=30)),
            ],
        ),
    ]