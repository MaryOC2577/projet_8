# Generated by Django 3.2.7 on 2021-11-11 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutella', '0002_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=400, unique=True),
        ),
    ]
