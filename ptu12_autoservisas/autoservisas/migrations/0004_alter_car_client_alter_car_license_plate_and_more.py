# Generated by Django 4.2.1 on 2023-05-30 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoservisas', '0003_alter_order_options_remove_order_sum_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='client',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Client'),
        ),
        migrations.AlterField(
            model_name='car',
            name='license_plate',
            field=models.CharField(db_index=True, max_length=50, verbose_name='License plate Nr.'),
        ),
        migrations.AlterField(
            model_name='car',
            name='vin_code',
            field=models.CharField(db_index=True, max_length=50, verbose_name='VIN code'),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='brand',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Make'),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='model',
            field=models.CharField(db_index=True, max_length=50, verbose_name='Model'),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='year',
            field=models.IntegerField(blank=True, db_index=True, null=True, verbose_name='Year'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(auto_now_add=True, db_index=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='orderentry',
            name='price',
            field=models.DecimalField(db_index=True, decimal_places=2, max_digits=18, null=True, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='orderentry',
            name='quantity',
            field=models.CharField(blank=True, db_index=True, max_length=50, null=True, verbose_name='Quantity'),
        ),
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(db_index=True, max_length=150, verbose_name='Service Name'),
        ),
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.DecimalField(db_index=True, decimal_places=2, max_digits=18, null=True, verbose_name='Price'),
        ),
    ]