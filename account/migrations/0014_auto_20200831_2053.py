# Generated by Django 3.1 on 2020-08-31 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_userdetails_both_parent_paid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdetails',
            old_name='both_parent_paid',
            new_name='grandparent_paid',
        ),
        migrations.AddField(
            model_name='userdetails',
            name='parent_paid',
            field=models.BooleanField(default=False),
        ),
    ]
