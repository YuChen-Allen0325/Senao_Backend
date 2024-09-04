# Generated by Django 4.2 on 2024-09-04 12:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redirection', '0011_rename_short_url_urlmapping_short_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlmapping',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 4, 20, 10, 1, 670635)),
        ),
        migrations.AlterField(
            model_name='urlmapping',
            name='short_code',
            field=models.CharField(max_length=6, unique=True),
        ),
    ]
