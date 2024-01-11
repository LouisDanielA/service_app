from django.urls import path

from services.views import SubscriptionView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api/subscriptions', SubscriptionView)

urlpatterns = [
    *router.urls,
]
