from django.shortcuts import render
from django.http import HttpResponse
from .models import Service, Car, OrderEntry
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