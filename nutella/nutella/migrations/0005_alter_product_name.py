# Generated by Django 3.2.7 on 2021-12-23 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutella', '0004_auto_20211215_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
