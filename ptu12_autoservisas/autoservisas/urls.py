from django.urls import path
from . import views
from .views import index, car_list, car_detail, OrderListView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("cars/", views.car_list, name="car_list"),
    path("car_detail/<int:pk>/", views.car_detail, name="car_detail"), 
    path("orders/", views.OrderListView.as_view(), name="order_list_view"),
    path("orders/<int:pk>/", views.OrderDetailView.as_view(), name="order_detail"),
    
] + (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))


