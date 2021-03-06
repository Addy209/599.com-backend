# Generated by Django 3.1 on 2020-08-26 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_delete_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbankdetails',
            name='account_number',
            field=models.CharField(default=55, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userbankdetails',
            name='account_holder_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='userpersonaldetails',
            name='pan',
            field=models.CharField(blank=True, max_length=25, unique=True),
        ),
    ]
