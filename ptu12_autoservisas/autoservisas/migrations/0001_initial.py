# Generated by Django 4.2.1 on 2023-05-30 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_plate', models.CharField(db_index=True, max_length=50, verbose_name='Valstybinis Nr.')),
                ('vin_code', models.CharField(db_index=True, max_length=50, verbose_name='VIN kodas')),
                ('client', models.CharField(db_index=True, max_length=100, verbose_name='Klientas')),
            ],
            options={
                'verbose_name': 'car',
                'verbose_name_plural': 'cars',
                'ordering': ['client', 'license_plate'],
            },
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(db_index=True, max_length=100, verbose_name='Markė')),
                ('model', models.CharField(db_index=True, max_length=50, verbose_name='Modelis')),
            ],
            options={
                'verbose_name': 'car model',
                'verbose_name_plural': 'car models',
                'ordering': ['brand', 'model'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, db_index=True, verbose_name='Data')),
                ('sum', models.DecimalField(db_index=True, decimal_places=2, max_digits=18, null=True, verbose_name='Suma')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='autoservisas.car', verbose_name='car')),
            ],
            options={
                'verbose_name': 'order',
                'verbose_name_plural': 'orders',
                'ordering': ['date'],
            },
        ),
        migrations.AddField(
            model_name='car',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='autoservisas.carmodel', verbose_name='model'),
        ),
    ]
