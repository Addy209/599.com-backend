# Generated by Django 3.0.4 on 2020-08-08 07:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clubs', '0002_delete_club'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grandparent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='grandparent', to=settings.AUTH_USER_MODEL)),
                ('l_child', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='left_Child', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='parent', to=settings.AUTH_USER_MODEL)),
                ('r_child', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='right_Child', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
