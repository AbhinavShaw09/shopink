from django.contrib import admin
from .models import Seller, Buyer, Order, OrderItem, Product, OrderPaymentRequest, PaymentWebhookEvent
# Register your models here.

admin.site.register(Seller)
admin.site.register(Buyer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Product)
admin.site.register(OrderPaymentRequest)
admin.site.register(PaymentWebhookEvent)

