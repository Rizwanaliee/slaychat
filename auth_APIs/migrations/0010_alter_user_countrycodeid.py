# Generated by Django 4.1.2 on 2022-10-20 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth_APIs', '0009_alter_user_devicetypeid_alter_user_usertypeid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='countryCodeId',
            field=models.ForeignKey(db_column='countryCodeId', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='countryCode_ref', to='auth_APIs.allcountries'),
        ),
    ]
