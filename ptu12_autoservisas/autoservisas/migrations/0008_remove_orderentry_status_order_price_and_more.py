# Generated by Django 4.2.1 on 2023-06-04 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoservisas', '0007_car_cover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderentry',
            name='status',
        ),
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=18, verbose_name='Price'),
        ),
        migrations.AddField(
            model_name='orderentry',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=18, verbose_name='Total'),
        ),
        migrations.AddField(
            model_name='service',
            name='status',
            field=models.CharField(choices=[('new', 'New'), ('processing', 'Processing'), ('complete', 'Complete'), ('cancelled', 'Cancelled')], db_index=True, default='new', max_length=20, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='car',
            name='client',
            field=models.CharField(max_length=100, verbose_name='Client'),
        ),
        migrations.AlterField(
            model_name='orderentry',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=18, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='orderentry',
            name='quantity',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=18, verbose_name='Quantity'),
        ),
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=18, null=True, verbose_name='Price'),
        ),
    ]