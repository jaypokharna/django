# Generated by Django 4.2.5 on 2023-09-26 17:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0014_alter_studentrank_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='reci',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2023, 9, 26, 17, 47, 17, 144496, tzinfo=datetime.timezone.utc), unique=True),
            preserve_default=False,
        ),
    ]
