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
from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response


class CategoriesViews(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class ProductsViews(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class LikeViews(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def create(self, request, *args, **kwargs):
        user = request.data.get('user_id')
        product = request.data.get('product')
        serializer = self.get_serializer(data=request.data)
        exists_like = Like.objects.filter(user_id=user, product=product)
        serializer.is_valid(raise_exception=True)
        if exists_like:
            exists_like.delete()
        else:
            self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CommentsViews(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

    def perform_create(self, serializer):
        id = self.kwargs.get('id')
        product = get_object_or_404(Products, id=id)
        user = self.request.user
        serializer.save(product=product, user=user)
