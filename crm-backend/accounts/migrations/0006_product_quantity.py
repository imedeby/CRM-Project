# Generated by Django 3.1.6 on 2021-02-17 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20210216_0807'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.FloatField(null=True),
        ),
    ]
