# Generated by Django 4.1.5 on 2023-04-16 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='datetime_of_appointment',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='datetime_of_booking',
            field=models.DateField(auto_now_add=True),
        ),
    ]
