# Generated by Django 3.1.7 on 2021-06-20 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0027_auto_20210620_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='end_date',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]