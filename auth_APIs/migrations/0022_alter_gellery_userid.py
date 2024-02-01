# Generated by Django 4.1.2 on 2022-11-14 06:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth_APIs', '0021_gellery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gellery',
            name='userId',
            field=models.ForeignKey(db_column='userId', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='doer_gellery_ref', to=settings.AUTH_USER_MODEL),
        ),
    ]
