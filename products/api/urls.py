from .views import (
    CategoriesViews,
    ProductsViews,
    LikeViews,
    CommentsViews)
from django.urls import path, include
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register("category", CategoriesViews, basename="category")
router.register("products", ProductsViews, basename="products")
router.register("like", LikeViews, basename="like")
router.register("comments", CommentsViews, basename="comments")


urlpatterns = [
    path("", include(router.urls))
]
