from typing import Any
from django.db.models.query import QuerySet
from django.db.models import Q 
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Service, Car, OrderEntry, CarModel, Order
from django.views import View , generic
from django.views.generic import ListView
# Create your views here.

def index(request):
    num_service = Service.objects.all().count()
    num_car = Car.objects.all().count()
    num_completed_services = Service.objects.filter(status="complete").count()

    num_visits = request.session.get("num_visits", 1)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_service" : num_service,
        "num_car" : num_car,
        "num_completed_services" : num_completed_services,
        "num_visits" : num_visits
    }
    return render(request, "autoservisas/index.html", context)

    

def car_list(request):
    qs = Car.objects
    query = request.GET.get("query")
    if query:
        qs = qs.filter(
            Q(model__brand__istartswith=query) |
            Q(client__istartswith=query) |
            Q(model__model__istartswith=query)
            
        )
    else:
        qs = qs.all()
    paginator = Paginator(qs, 3)
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
    
    def get_queryset(self) -> QuerySet[Any]:
        qs = super().get_queryset()
        query = self.request.GET.get("query")
        if query:
            qs = qs.filter(
                Q(car__client__istartswith=query) |
                Q(car__license_plate__istartswith=query) |
                Q(car__vin_code__istartswith=query) |
                Q(car__model__model__icontains=query) |
                Q(car__model__brand__icontains=query)
            )
        return qs



class OrderDetailView(generic.DetailView):
    model = Order
    template_name = "autoservisas/order_detail.html"
    context_object_name = "order"
    
    def get_queryset(self):
        return super().get_queryset().prefetch_related("order_entries")
