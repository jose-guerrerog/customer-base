# Generated by Django 2.2.4 on 2019-08-30 04:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20190830_0359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datasheet',
            name='historical_data',
        ),
    ]
