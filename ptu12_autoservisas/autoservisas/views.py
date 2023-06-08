from typing import Any, Dict
from django.db.models.query import QuerySet
from django.db.models import Q
from django.http import HttpResponse 
from django.shortcuts import render, get_object_or_404, reverse
from django.core.paginator import Paginator
from .models import Service, Car, OrderEntry, CarModel, Order
from django.views import View , generic
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from . forms import OrderReviewForm
# Create your views here.

def index(request):
    num_service = Service.objects.all().count()
    num_car = Car.objects.all().count()
    num_completed_services = OrderEntry.objects.filter(status="complete").count()

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
    paginator = Paginator(qs, 5)
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
                Q(car__client__icontains=query) |
                Q(car__license_plate__istartswith=query) |
                Q(car__vin_code__istartswith=query) |
                Q(car__model__model__icontains=query) |
                Q(car__model__brand__icontains=query)
            )
        return qs



class OrderDetailView(generic.edit.FormMixin, generic.DetailView):
    model = Order
    template_name = "autoservisas/order_detail.html"
    context_object_name = "order"
    form_class = OrderReviewForm
    
    def get_initial(self) -> Dict[str, Any]:
        initial = super().get_initial()
        initial["order"] = self.get_object()
        initial["reviewer"] = self.request.user
        return initial
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        
    def form_valid(self, form: Any) -> HttpResponse:
        form.instance.order = self.get_object()
        form.instance.reviewer = self.request.user
        form.save()
        messages.success(self.request, _("Comment posted."))
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse("order_detail", kwargs={"pk":self.get_object().pk})

    def get_queryset(self):
        return super().get_queryset().prefetch_related("order_entries")
    

class UserOrderEntryListView(LoginRequiredMixin, generic.ListView):
    model = Order
    template_name = "autoservisas/my_orders.html"
    paginate_by = 5

    def get_queryset(self) -> QuerySet[Any]:
        qs = super().get_queryset()
        qs = qs.filter(car__client=self.request.user)
        return qs

# @login_required
# def my_orders(request):
#     user = request.user
#     orders = Order.objects.filter(car__user_field=user)
#     return render(request, "autoservisas/my_orders.html", {"orders":orders})



 
