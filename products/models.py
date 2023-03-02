from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Categories(models.Model):
    name = models.CharField(max_length=20)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Products(models.Model):
    category = models.ForeignKey(
        Categories, on_delete=models.PROTECT, related_name="Category")
    name = models.CharField(max_length=20)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to="profiles_photo/%Y/%m/%d/")
    stock = models.IntegerField()
    size = models.CharField(
        help_text="Size of products, example S-M-L-XL or 45-39", max_length=10, blank=True, null=True)
    amount = models.CharField(
        help_text="Size of products, example 500g - 1kg", max_length=10, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Products"


class Like(models.Model):
    product = models.ForeignKey(
        Products, on_delete=models.CASCADE, related_name="like_product")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="like_user")
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'this is like on {self.product.name}'


class Comments(models.Model):
    product = models.ForeignKey(
        Products, on_delete=models.CASCADE, related_name="comments_product")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments_user")
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'this is comments on {self.product.name}'

    class Meta:
        verbose_name_plural = "Comments"
