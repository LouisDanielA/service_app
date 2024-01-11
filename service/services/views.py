from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import *
from .serializers import SubscriptionSerializer


class SubscriptionView(ReadOnlyModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer



