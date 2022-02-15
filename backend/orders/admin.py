from django.contrib import admin

from orders.models import Order, OrderItem, Invoice, Payment


class OrderAdmin(admin.ModelAdmin):

    class Meta:
        model = Order


class OrderItemAdmin(admin.ModelAdmin):

    class Meta:
        model = OrderItem


class InvoiceAdmin(admin.ModelAdmin):

    class Meta:
        model = Invoice


class PaymentAdmin(admin.ModelAdmin):

    class Meta:
        model = Payment


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Payment, PaymentAdmin)
