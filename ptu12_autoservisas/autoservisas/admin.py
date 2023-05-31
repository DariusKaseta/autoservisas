from django.contrib import admin
from . import models
from .models import OrderEntry


class OrderEntryInline(admin.TabularInline):
    model = OrderEntry

class OrderEntryAdmin(admin.ModelAdmin):
    list_display = ("service", "order", "quantity", "price")

class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "car", "date")
    inlines = [OrderEntryInline]

class CarAdmin(admin.ModelAdmin):
    list_display = (
        "id", "model", "license_plate", 
        "vin_code", "client")
    list_filter = ("client", "model")
    search_fields = ("license_plate", "vin_code")

class ServiceAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price")


admin.site.register(models.Car, CarAdmin)
admin.site.register(models.CarModel)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.OrderEntry, OrderEntryAdmin)
admin.site.register(models.Service, ServiceAdmin)

