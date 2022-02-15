from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models

from products.models import Product

User = get_user_model()


class OrderStatusCodeChoices(models.TextChoices):
    STARTED = 'started'
    PROCESSING = 'processing'
    READY_TO_SHIP = 'ready_to_ship'
    DELIVERED = 'delivered'
    CANCELLED = 'cancelled'
    SHOP_FAILED = 'shop_failed'
    DECLINED = 'declined'


class OrderItemStatusCodeChoices(models.TextChoices):
    STARTED = 'started'


class InvoiceStatusCodeChoices(models.TextChoices):
    PAID = 'paid'
    WAITING = 'waiting'
    DECLINED = 'declined'


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    status_code = models.CharField(
        choices=OrderStatusCodeChoices.choices, default=OrderStatusCodeChoices.STARTED, max_length=250)
    status_description = models.TextField()
    date_order_placed = models.DateField(default=datetime.now)
    order_details = models.TextField()
    created_at = models.DateField(default=datetime.now)
    updated_at = models.DateField(default=datetime.now)
    shipment_tracking_id = models.SlugField(null=True, blank=False)
    shipment_date = models.DateField(null=True)
    shipment_details = models.TextField()

    # @property
    # def get_main_order_info(self) -> OrderedDict:
    #     result = OrderedDict()
    #     result


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False, blank=False)
    status_code = models.CharField(
        choices=OrderItemStatusCodeChoices.choices, default=OrderItemStatusCodeChoices.STARTED, max_length=250)
    quantity = models.PositiveIntegerField()
    price = models.FloatField()
    details = models.TextField()
    ordered_at = models.DateField(default=datetime.now)
    updated_at = models.DateField(default=datetime.now)


class Invoice(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False, blank=False)
    status_code = models.CharField(
        choices=InvoiceStatusCodeChoices.choices, default=InvoiceStatusCodeChoices.WAITING, max_length=250)
    status_description = models.TextField()
    details = models.TextField()
    invoice_date = models.DateField(default=datetime.now)


class Payment(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, null=False, blank=False)
    payment_date = models.DateField(default=datetime.now)
    payment_amount = models.FloatField()
