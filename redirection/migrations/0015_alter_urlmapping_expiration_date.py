# Generated by Django 4.2 on 2024-09-05 05:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redirection', '0014_alter_urlmapping_expiration_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlmapping',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 5, 13, 25, 18, 402202)),
        ),
    ]
