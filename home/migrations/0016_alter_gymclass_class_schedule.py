# Generated by Django 3.2.19 on 2023-07-08 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_alter_gymclass_class_schedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gymclass',
            name='class_schedule',
            field=models.CharField(max_length=20, null=True),
        ),
    ]