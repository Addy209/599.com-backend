# Generated by Django 3.1 on 2020-08-30 16:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_auto_20200826_1156'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegistrationStatusDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_status', models.CharField(choices=[['unpaid', 'unpaid'], ['pending', 'pending'], ['paid', 'paid']], default='unpaid', max_length=255)),
                ('ss_url', models.URLField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]