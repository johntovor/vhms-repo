# Generated by Django 4.1.5 on 2023-01-20 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0004_alter_appointment_appointment_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='appointment_time',
            field=models.TimeField(null=True),
        ),
    ]
