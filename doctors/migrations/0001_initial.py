# Generated by Django 4.1.5 on 2023-01-20 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, max_length=300, null=True)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='departments.department')),
            ],
            options={
                'ordering': ('-date_added',),
            },
        ),
    ]
