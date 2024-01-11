from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from clients.models import Client


# from service.clients.models import Client


# from clients.models import Client

class Service(models.Model):
    name = models.CharField(max_length=50, blank=False, null=True)
    full_price = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Сервис"
        verbose_name_plural = "Сервисы"


class Plan(models.Model):
    PLAN_TYPES = (
        ('full', 'full'),
        ('student', 'student'),
        ('discount', 'discount'),
    )
    plan_type = models.CharField(choices=PLAN_TYPES, max_length=10)
    discount_percent = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])

    def __str__(self):
        return self.plan_type

    class Meta:
        verbose_name = "План"
        verbose_name_plural = "Планы"


class Subscription(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='subscriptions')
    service = models.ForeignKey(Service, on_delete=models.PROTECT, related_name='services')
    plan = models.ForeignKey(Plan, on_delete=models.PROTECT, related_name='plans')

    def __str__(self):
        return self.client.user.get_full_name()

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
