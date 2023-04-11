# Generated by Django 4.2 on 2023-04-09 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0003_alter_schedule_equipment_alter_schedule_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='equipment',
            field=models.CharField(choices=[('Desktop Computers', 'Desktop Computers'), ('Soldering Stations', 'Soldering Stations'), ('Electronics Station', 'Electronics Stations'), ('Lasers', 'Lasers'), ('3D Printers', '3D Printers'), ('CNC Machine', 'CNC Machine'), ('Vacuum Former', 'Vacuum Former'), ('Vinyl Cutter', 'Vinyl Cutter'), ('Heat Press', 'Heat Press'), ('Assembly Stations', 'Assembly Stations'), ('Photo Studio', 'Photo Studio'), ('Format Printer', 'Format Printer')], default='Desktop Computers', max_length=50),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='time',
            field=models.CharField(choices=[('8 AM', '8 AM'), ('10 AM', '10 AM'), ('12 AM', '12 AM'), ('2 PM', '2 PM'), ('4 PM', '4 PM'), ('6 PM', '6 PM'), ('8 PM', '8 PM')], default='2 PM', max_length=10),
        ),
    ]
