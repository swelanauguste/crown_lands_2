# Generated by Django 3.2.5 on 2021-07-17 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0007_auto_20210717_0614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individualapplication',
            name='application_type',
            field=models.CharField(default='PURCHASE', max_length=255),
        ),
    ]
