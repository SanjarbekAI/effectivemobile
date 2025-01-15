from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel

UserModel = get_user_model()


class OrderModel(BaseModel):
    class OrderStatus(models.TextChoices):
        WAITING = 'WAITING', 'Waiting'
        PAID = 'PAID', 'Paid'
        CANCELED = 'CANCELED', 'Canceled'

    status = models.CharField(
        max_length=20,
        choices=OrderStatus.choices,
        default=OrderStatus.WAITING,
        verbose_name=_('status')
    )
    cashier = models.ForeignKey(
        UserModel,
        on_delete=models.PROTECT,
        related_name='orders',
        verbose_name=_('cashier')
    )
    table_number = models.PositiveIntegerField(
        unique=True, verbose_name=_('table number'))
    total_price = models.DecimalField(
        max_digits=20, decimal_places=2,
        verbose_name=_('total price')
    )

    class Meta:
        unique_together = ['status', 'table_number']


class OrderItem(BaseModel):
    class OrderItemStatus(models.TextChoices):
        WAITING = 'WAITING', 'Waiting'
        PREPARED = 'PREPARED', 'Prepared'
        CANCELED = 'CANCELED', 'Canceled'

    status = models.CharField(
        max_length=20,
        choices=OrderItemStatus.choices,
        default=OrderItemStatus.WAITING,
        verbose_name=_('status')
    )
    product_image = models.ImageField(
        upload_to='products/',
        null=True, blank=True,
        verbose_name=_('image')
    )
    product_name = models.CharField(
        max_length=255, verbose_name=_('product name')
    )
    product_quantity = models.PositiveSmallIntegerField(default=1)
    product_price = models.DecimalField(max_digits=20, decimal_places=2)
    total_price = models.DecimalField(
        max_digits=20, decimal_places=2,
        verbose_name=_('total price')
    )
    order = models.ForeignKey(
        OrderModel,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name=_('order')
    )
