# Generated by Django 4.2.3 on 2023-09-21 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0011_alter_studentrank_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentrank',
            name='date_of_report_card_generation',
            field=models.DateField(auto_now_add=True),
        ),
    ]
