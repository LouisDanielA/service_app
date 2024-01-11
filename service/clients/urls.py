from django.urls import path
from .views import ClientAPIView



urlpatterns = [
    path('api/clients/', ClientAPIView.as_view())
]