# Generated by Django 3.2.19 on 2023-07-08 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_gymclass_class_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='gymlocation',
            name='schedule',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='schedule', to='home.gymclass'),
        ),
    ]
