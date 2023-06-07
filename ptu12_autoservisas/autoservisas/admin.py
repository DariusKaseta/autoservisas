from django.contrib import admin
from . import models
from .models import OrderEntry

class CarModelAdmin(admin.ModelAdmin):
    list_display = ("brand", "model", "year")


class OrderEntryInline(admin.TabularInline):
    model = OrderEntry
    extra = 0

class OrderEntryAdmin(admin.ModelAdmin):
    list_display = ("service", "order", "quantity", "price")

class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "car", "date")
    inlines = [OrderEntryInline]

class CarModelAdmin(admin.ModelAdmin):
    list_display = ("id", "make", "model", "year")

class CarAdmin(admin.ModelAdmin):
    list_display = (
        "id", "model", "license_plate", 
        "vin_code", "client")
    list_filter = ("model",)
    search_fields = ("license_plate", "vin_code", "due_back")

class ServiceAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price")

class OrderReviewAdmin(admin.ModelAdmin):
    list_display = ("reviewed_at", "order", "reviewer", "content")

admin.site.register(models.Car, CarAdmin)
admin.site.register(models.CarModel)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.OrderEntry, OrderEntryAdmin)
admin.site.register(models.Service, ServiceAdmin)
admin.site.register(models.UserOrderReview, OrderReviewAdmin)
