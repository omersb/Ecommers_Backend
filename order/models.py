from products.models import Products
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class OrderItem():
    product = models.ManyToManyField(
        Products, related_name="product", on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


class PaymentMethod():
    method = models.In
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


class Order(models.Model):
    order_name = models.CharField(max_length=25)
    user = models.OneToOneField(
        User, related_name="order", on_delete=models.CASCADE)
    order_item = models.ManyToManyField(
        OrderItem, related_name="order_item", on_delete=models.PROTECT)
    payment_method = models.OneToOneField(
        PaymentMethod, related_name="payment_method", on_delete=models.PROTECT)
    sub_total_price = models.IntegerField()
    tax_price = models.IntegerField()
    shipping_price = models.IntegerField()
    total_price = models.IntegerField()
    is_paid = models.BooleanField()
    paid_at = models.DateTimeField()
    is_delivered = models.BooleanField()
    delivered_at = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.order_name
