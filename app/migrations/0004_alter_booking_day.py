# Generated by Django 4.2.1 on 2023-12-21 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_booking_time_slot_booking_day_delete_turf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='day',
            field=models.CharField(choices=[('mon', 'Monday'), ('tue', 'Tuesday'), ('wed', 'Wednesday'), ('thu', 'Thursday'), ('fri', 'Friday'), ('sat', 'Saturday'), ('sun', 'Sunday')], default='mon', max_length=3, null=True),
        ),
    ]
