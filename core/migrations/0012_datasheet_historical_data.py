# Generated by Django 2.2.4 on 2019-08-31 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_remove_datasheet_historical_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='datasheet',
            name='historical_data',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
