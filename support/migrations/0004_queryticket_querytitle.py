# Generated by Django 4.1.2 on 2023-02-13 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0003_favouritedoer'),
    ]

    operations = [
        migrations.AddField(
            model_name='queryticket',
            name='queryTitle',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
