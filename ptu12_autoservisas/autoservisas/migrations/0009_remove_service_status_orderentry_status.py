# Generated by Django 4.2.1 on 2023-06-06 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoservisas', '0008_remove_orderentry_status_order_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='status',
        ),
        migrations.AddField(
            model_name='orderentry',
            name='status',
            field=models.CharField(choices=[('new', 'New'), ('processing', 'Processing'), ('complete', 'Complete'), ('cancelled', 'Cancelled')], db_index=True, default='new', max_length=20, verbose_name='Status'),
        ),
    ]
