# Generated by Django 4.2.3 on 2023-08-29 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.TextField()),
                ('email', models.TextField()),
                ('phnumber', models.IntegerField()),
                ('password', models.TextField()),
            ],
        ),
    ]
