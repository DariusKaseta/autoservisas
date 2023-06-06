# Generated by Django 4.2.1 on 2023-06-06 08:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('autoservisas', '0010_alter_car_options_remove_car_client_order_due_back'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cars', to=settings.AUTH_USER_MODEL, verbose_name='client'),
        ),
    ]