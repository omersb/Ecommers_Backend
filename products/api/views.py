from ..models import (
    Products,
    Categories,
    Like,
    Comments)
from .serializers import (
    ProductsSerializer,
    CategoriesSerializer,
    LikeSerializer,
    CommentsSerializer)
from rest_framework import generics, viewsets


class CategoriesViews(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
