# Generated by Django 4.2 on 2024-09-04 07:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redirection', '0008_alter_urlmapping_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlmapping',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 4, 15, 39, 2, 83706)),
        ),
    ]
