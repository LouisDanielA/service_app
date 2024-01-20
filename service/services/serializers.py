from rest_framework import serializers

from services.models import Subscription, Plan


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ('__all__')


class SubscriptionSerializer(serializers.ModelSerializer):
    plan = PlanSerializer()
    client_name = serializers.CharField(source='client.company_name')
    email = serializers.CharField(source='client.user.email')
    price = serializers.SerializerMethodField()

    def get_price(self, instance):
        # print('self', self)
        return instance.price
    #     return (obj.service.full_price -
                # (obj.service.full_price *
    #              (obj.plan.discount_percent / 100)))

    class Meta:
        model = Subscription
        fields = ['id', 'client_name', 'email', 'plan_id', 'plan', 'price']
