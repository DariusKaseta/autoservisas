from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Service, Car, OrderEntry, CarModel, Order
from django.views import View , generic
from django.views.generic import ListView


# Create your views here.

def index(request):
    num_service = Service.objects.all().count()
    num_car = Car.objects.all().count()
    num_completed_services = OrderEntry.objects.filter(status="complete").count()

    context = {
        "num_service" : num_service,
        "num_car" : num_car,
        "num_completed_services" : num_completed_services,
    }
    return render(request, "autoservisas/index.html", context)

def car_list(request):
    paginator = Paginator(Car.objects.all(), 3)
    car_list = paginator.get_page(request.GET.get("page"))
    return render(request, "autoservisas/car_list.html", {
        "car_list" : car_list,
    })

def car_detail(request, pk: int):
    car_detail = get_object_or_404(Car, pk=pk)
    context = {
        "car" : car_detail
    }
    return render(request, "autoservisas/car_detail.html", context)

class OrderListView(generic.ListView):
    model = Order
    paginate_by = 5
    context_object_name = "orders"
    template_name = "autoservisas/order_list_view.html"
    
    def get_queryset(self):
        return super().get_queryset().prefetch_related("order_entries")

class OrderDetailView(generic.DetailView):
    model = Order
    template_name = "autoservisas/order_detail.html"
    context_object_name = "order"
    
    def get_queryset(self):
        return super().get_queryset().prefetch_related("order_entries")


# def order_detail(request, pk):
#     order = get_object_or_404(Order, pk=pk)
#     context = {
#         "order" : order
#     }
#     return render(request, "autoservisas/order_detail.html", context)