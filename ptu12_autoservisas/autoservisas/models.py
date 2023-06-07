from typing import Any, Iterable, Optional
from django.db import models
from django.utils.translation import gettext_lazy as _ 
from django.urls import reverse
from datetime import date
from django.contrib.auth import get_user_model
from tinymce.models import HTMLField

User = get_user_model()

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
    client = models.ForeignKey(
        User, 
        verbose_name=_("client"), 
        related_name="cars", 
        on_delete=models.CASCADE, null=True, blank=True)
    license_plate = models.CharField(_("License plate Nr."), max_length=50, db_index=True)
    model = models.ForeignKey(
        CarModel, 
        verbose_name=_("model"), 
        on_delete=models.CASCADE,
        related_name="cars")
    vin_code =  models.CharField(_("VIN code"), max_length=50, db_index=True)
    description = HTMLField(_("Description"), max_length=10000, null=True, blank=True)

    cover = models.ImageField(
        _("cover"), upload_to="autoservisas/car_covers",
        null=True, blank=True,
    )

    class Meta:
        ordering = ["model", 'license_plate']
        verbose_name = _("car")
        verbose_name_plural = _("cars")

    def __str__(self):
        return f"{self.license_plate}"

    def get_absolute_url(self):
        return reverse("car_detail", kwargs={"pk": self.pk})
    
    
class Order(models.Model):
    date = models.DateField(_("Date"), auto_now=False, auto_now_add=True, db_index=True)
    price = models.DecimalField(_("Price"), max_digits=18, decimal_places=2, default=0, null=True)
    car = models.ForeignKey(
        Car, 
        verbose_name=_("car"), 
        on_delete=models.CASCADE,
        related_name="orders")
    
    due_back = models.DateField(_("Due back"), null=True, blank=True, db_index=True)

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False
    
    class Meta:
        ordering = ['date', "id"]
        verbose_name = _("order")
        verbose_name_plural = _("orders")

    def __str__(self):
        return f"No. - {self.car} - { self.car.model.model}"

    def get_absolute_url(self):
        return reverse("order_detail", kwargs={"pk": self.pk})
    
    @property
    def client(self):
        return self.car.client

class Service(models.Model):
    name = models.CharField(_("Service Name"), max_length=150, db_index=True)
    price = models.DecimalField(_("Price"), max_digits=18, decimal_places=2, null=True)
    
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
        related_name="order_entries",
        on_delete=models.CASCADE, null=True)
    quantity = models.DecimalField(_("Quantity"),max_digits=18, decimal_places=2, default=1)
    price = models.DecimalField(_("Price"), max_digits=18, decimal_places=2, default=0)
    total = models.DecimalField(_("Total"), max_digits=18, decimal_places=2, default=0)
    
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
    
    def get_color(self):
        colors = {
            "new": "blue",
            "processing": "orange",
            "complete": "green",
            "cancelled": "red",
        }
        default_color = "black"
        return colors.get(self.status, default_color)

    def get_status_display(self):
        return dict(self.STATUS_CHOICES).get(self.status)

    def save(self, *args, **kwargs):
        if self.price == 0:
            self.price = self.service.price
        if self.status != "cancelled":  # Skip calculating total if service is cancelled
            self.total = self.price * self.quantity
        super().save(*args, **kwargs)
        self.order.price = self.order.order_entries.exclude(status="cancelled").aggregate(models.Sum("total"))["total__sum"]
        self.order.save()

class UserOrderReview(models.Model):
    order = models.ForeignKey(
        Order,
        verbose_name=_("order"),
        on_delete=models.CASCADE,
        related_name="reviews",
    )

    reviewer = models.ForeignKey(
        User,
        verbose_name=_("reviewer"),
        on_delete=models.SET_NULL,
        related_name="user_order_review",
        null=True, blank=True,
    )   
    reviewed_at = models.DateTimeField(_("Reviewed"), auto_now_add=True)
    content = models.TextField(_("content"), max_length=4000)

    class Meta:
        ordering = ["-reviewed_at"]
        verbose_name = _("user order review")
        verbose_name_plural = _("user order reviews")

    def __str__(self):
        return f"{self.reviewed_at}: {self.reviewer}"

    def get_absolute_url(self):
        return reverse("userorderreview_detail", kwargs={"pk": self.pk})


