from products.models import Products
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class OrderItem(models.Model):
    product = models.OneToOneField(
        Products, related_name="product", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name


class PaymentMethod(models.Model):
    method = models.CharField(max_length=30)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.method


class Order(models.Model):
    order_name = models.CharField(max_length=25)
    user = models.OneToOneField(
        User, related_name="order", on_delete=models.CASCADE)
    order_item = models.ForeignKey(
        OrderItem, related_name="order_item", on_delete=models.PROTECT)
    payment_method = models.ForeignKey(
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
