# Generated by Django 3.2.19 on 2023-06-28 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attendance',
            options={'verbose_name_plural': 'Attendance'},
        ),
        migrations.AlterModelOptions(
            name='gymlocation',
            options={'verbose_name_plural': 'GymLocation'},
        ),
        migrations.AlterModelOptions(
            name='paymentoption',
            options={'verbose_name_plural': 'PaymentOption'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name_plural': 'User'},
        ),
    ]
