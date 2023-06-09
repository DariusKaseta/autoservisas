# Generated by Django 4.2.1 on 2023-06-07 08:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('autoservisas', '0013_alter_car_options_remove_car_due_back_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='user_field',
        ),
        migrations.AddField(
            model_name='car',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cars', to=settings.AUTH_USER_MODEL, verbose_name='client'),
        ),
        migrations.CreateModel(
            name='UserOrderReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewed_at', models.DateTimeField(auto_now_add=True, verbose_name='Reviewed')),
                ('content', models.TextField(max_length=4000, verbose_name='content')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='autoservisas.order', verbose_name='order')),
                ('reviewer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_order_review', to=settings.AUTH_USER_MODEL, verbose_name='reviewer')),
            ],
            options={
                'verbose_name': 'user order review',
                'verbose_name_plural': 'user order reviews',
                'ordering': ['-reviewed_at'],
            },
        ),
    ]
