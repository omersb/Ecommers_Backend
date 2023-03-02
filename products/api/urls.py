from .views import CategoriesViews
from django.urls import path, include
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register("category", CategoriesViews, basename="category")


urlpatterns = [
    path("", include(router.urls))
]
