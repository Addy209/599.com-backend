# Generated by Django 3.1 on 2020-08-31 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_userregistrationstatusdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='both_parent_paid',
            field=models.BooleanField(default=False),
        ),
    ]
