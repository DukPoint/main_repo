# Generated by Django 4.2.7 on 2023-11-29 02:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='user',
            table='accounts',
        ),
    ]