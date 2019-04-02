# Generated by Django 2.1.7 on 2019-04-02 15:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_buyvehicle'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyvehicle',
            name='city',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buyvehicle',
            name='p_number',
            field=models.CharField(default=6628987676, max_length=10, validators=[django.core.validators.RegexValidator(regex='^(\\+\\d{1,2}\\s)?\\(?\\d{3}\\)?[\\s.-]\\d{3}[\\s.-]\\d{4}$')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buyvehicle',
            name='state',
            field=models.TextField(default='MS'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buyvehicle',
            name='street',
            field=models.TextField(default='123 Askew Street'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buyvehicle',
            name='z_code',
            field=models.IntegerField(default=44334),
            preserve_default=False,
        ),
    ]
