# Generated by Django 2.2.6 on 2019-11-02 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_auto_20191102_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner_ship',
            name='name',
            field=models.CharField(default='mane', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='owner_ship',
            name='price',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]