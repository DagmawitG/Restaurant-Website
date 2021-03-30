# Generated by Django 3.0.5 on 2021-03-28 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0032_auto_20210328_1810'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('your_name', models.CharField(max_length=50)),
                ('your_phone', models.CharField(max_length=50)),
                ('your_email', models.EmailField(max_length=50)),
                ('date', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=50)),
                ('number_of_people', models.EmailField(max_length=50)),
                ('message', models.CharField(max_length=2000)),
            ],
        ),
    ]