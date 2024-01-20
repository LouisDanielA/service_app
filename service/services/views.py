from django.db.models import Prefetch, F, Aggregate, Sum
from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import *
from .serializers import SubscriptionSerializer


class SubscriptionView(ReadOnlyModelViewSet):
    # queryset = Subscription.objects.all().prefetch_related('client').prefetch_related('client__user')
    queryset = Subscription.objects.all().prefetch_related(
        Prefetch('client', queryset=Client.objects.all().select_related('user').only('company_name', 'user__email')),
        'plan',
        # 'service'
    ).annotate(price=F('service__full_price')-
                     F('service__full_price') * F('plan__discount_percent')/100)
    serializer_class = SubscriptionSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response_data = {'result': response.data}
        response_data['full_price'] = self.queryset.aggregate(full_price=Sum('price')).get('full_price')
        # print('type price ', type(response_data['full_price']))
        response.data = response_data
        return response



