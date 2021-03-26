# Generated by Django 3.0.5 on 2021-03-26 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0025_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='content_1',
            field=models.TextField(default='', verbose_name='Event Content 1'),
        ),
        migrations.AddField(
            model_name='event',
            name='content_2',
            field=models.TextField(default='', verbose_name='Event Content 2'),
        ),
        migrations.AddField(
            model_name='event',
            name='content_3',
            field=models.TextField(default='', verbose_name='Event Content 3'),
        ),
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(default='', verbose_name='Event Description'),
        ),
        migrations.AlterField(
            model_name='event',
            name='content',
            field=models.TextField(verbose_name='Event Summary'),
        ),
    ]