# Generated by Django 3.0.5 on 2021-03-26 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_auto_20210326_1021'),
    ]

    operations = [
        migrations.AddField(
            model_name='footer',
            name='copyrightText',
            field=models.TextField(default="Copyright El Delicios d'Etiopia. All Rights Reserved", max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='footer',
            name='year',
            field=models.TextField(default='2021', max_length=100),
        ),
    ]
