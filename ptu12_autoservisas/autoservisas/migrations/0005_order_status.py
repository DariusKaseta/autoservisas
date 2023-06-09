# Generated by Django 4.2.1 on 2023-05-31 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoservisas', '0004_alter_car_client_alter_car_license_plate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('new', 'New'), ('processing', 'Processing'), ('complete', 'Complete'), ('cancelled', 'Cancelled')], db_index=True, default='new', max_length=20, verbose_name='Status'),
        ),
    ]
