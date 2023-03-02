from django.contrib import admin
from .models import Categories, Products, Like, Comments


admin.site.register(Categories)
admin.site.register(Products)
admin.site.register(Like)
admin.site.register(Comments)
