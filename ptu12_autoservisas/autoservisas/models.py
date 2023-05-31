from typing import Iterable, Optional
from django.db import models
from django.utils.translation import gettext_lazy as _ 
from django.urls import reverse

class CarModel(models.Model):
    brand = models.CharField(_("Make"), max_length=100, db_index=True)
    model = models.CharField(_("Model"), max_length=50, db_index=True)
    year = models.IntegerField(_("Year"), null=True, blank=True, db_index=True)

    class Meta:
        ordering = ['brand', 'model']
        verbose_name = _("car model")
        verbose_name_plural = _("car models")

    def __str__(self):
        return f"{self.brand} - {self.model}"

    def get_absolute_url(self):
        return reverse("carmodel_detail", kwargs={"pk": self.pk})


class Car(models.Model):
    license_plate = models.CharField(_("License plate Nr."), max_length=50, db_index=True)
    model = models.ForeignKey(
        CarModel, 
        verbose_name=_("model"), 
        on_delete=models.CASCADE,
        related_name="cars")
    vin_code =  models.CharField(_("VIN code"), max_length=50, db_index=True)
    client = models.CharField(_("Client"), max_length=100, db_index=True)

    class Meta:
        ordering = ['client', 'license_plate']
        verbose_name = _("car")
        verbose_name_plural = _("cars")

    def __str__(self):
        return f"{self.client} - {self.license_plate}"

    def get_absolute_url(self):
        return reverse("car_detail", kwargs={"pk": self.pk})
    
    
class Order(models.Model):
    date = models.DateField(_("Date"), auto_now=False, auto_now_add=True, db_index=True)
    car = models.ForeignKey(
        Car, 
        verbose_name=_("car"), 
        on_delete=models.CASCADE,
        related_name="orders")
    
    class Meta:
        ordering = ['date', "id"]
        verbose_name = _("order")
        verbose_name_plural = _("orders")

    def __str__(self):
        return f"Order #{self.id} - {self.date}"

    def get_absolute_url(self):
        return reverse("order_detail", kwargs={"pk": self.pk})


class Service(models.Model):
    name = models.CharField(_("Service Name"), max_length=150, db_index=True)
    price = models.DecimalField(_("Price"), max_digits=18, decimal_places=2, null=True, db_index=True)

    class Meta:
        ordering = ["name", "price"]
        verbose_name = _("service")
        verbose_name_plural = _("services")

    def __str__(self):
        return f"{self.name} - {self.price}"

    def get_absolute_url(self):
        return reverse("service_detail", kwargs={"pk": self.pk})


class OrderEntry(models.Model):
    service = models.ForeignKey(
        Service, 
        verbose_name=_("service"),
        related_name="order_entries", 
        on_delete=models.CASCADE, null=True)
    order = models.ForeignKey(
        Order, 
        verbose_name=_("order"),
        related_name ="order_entries",
        on_delete=models.CASCADE, null=True)
    quantity = models.CharField(_("Quantity"), max_length=50, null=True, blank=True, db_index=True)
    price = models.DecimalField(_("Price"), max_digits=18, decimal_places=2, null=True, db_index=True)

    STATUS_CHOICES = [
        ("new", "New"),
        ("processing", "Processing"),
        ("complete", "Complete"),
        ("cancelled", "Cancelled"),
    ]
    status = models.CharField(_("Status"), max_length=20, choices=STATUS_CHOICES, default="new", db_index=True)

    class Meta:
        ordering = ["price", "quantity"]
        verbose_name = _("order entry")
        verbose_name_plural = _("order entries")

    def __str__(self):
        return f"{self.service.name} - {self.quantity} - {self.price}"

    def get_absolute_url(self):
        return reverse("orderentry_detail", kwargs={"pk": self.pk})
    
    def save(self, *args, **kwargs):
        if self.price == 0:
            self.price = self.service.price
        super().save(*args, **kwargs)