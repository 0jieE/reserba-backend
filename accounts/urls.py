from django.urls import path
from .views import RegisterView, ShopCreateView, ServiceCreateView, BookingCreateView

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='user-register'),  # <- No longer under /users/
    path('shops/create/', ShopCreateView.as_view(), name='shop-create'),
    path('services/create/', ServiceCreateView.as_view(), name='service-create'),
    path('bookings/create/', BookingCreateView.as_view(), name='booking-create'),
]
