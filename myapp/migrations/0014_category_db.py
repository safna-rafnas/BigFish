# Generated by Django 3.1.4 on 2021-01-07 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_auto_20201228_1522'),
    ]

    operations = [
        migrations.CreateModel(
            name='category_db',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=50, null=True)),
                ('catdescpn', models.TextField(max_length=50, null=True)),
                ('image', models.ImageField(upload_to='catimage/')),
            ],
        ),
    ]
