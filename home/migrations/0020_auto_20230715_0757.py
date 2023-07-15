# Generated by Django 3.2.20 on 2023-07-15 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20230714_1940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipmentfacilities',
            name='changing_rooms',
        ),
        migrations.RemoveField(
            model_name='equipmentfacilities',
            name='free_parking',
        ),
        migrations.RemoveField(
            model_name='equipmentfacilities',
            name='lockers',
        ),
        migrations.RemoveField(
            model_name='equipmentfacilities',
            name='personal_trainer',
        ),
        migrations.RemoveField(
            model_name='equipmentfacilities',
            name='pool',
        ),
        migrations.RemoveField(
            model_name='equipmentfacilities',
            name='sauna',
        ),
        migrations.RemoveField(
            model_name='equipmentfacilities',
            name='sunbeds',
        ),
        migrations.AddField(
            model_name='equipmentfacilities',
            name='equipment_available',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
    ]