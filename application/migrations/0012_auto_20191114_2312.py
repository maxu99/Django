# Generated by Django 2.2.7 on 2019-11-14 23:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0011_reservation_renter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner_ship',
            name='date_in',
        ),
        migrations.RemoveField(
            model_name='owner_ship',
            name='date_out',
        ),
    ]