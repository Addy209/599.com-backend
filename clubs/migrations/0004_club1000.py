# Generated by Django 3.0.4 on 2020-08-08 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0003_club'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club1000',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='member', to='clubs.Club')),
            ],
        ),
    ]
