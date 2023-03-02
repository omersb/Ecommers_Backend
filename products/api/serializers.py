from rest_framework import serializers
from ..models import Categories, Products, Comments, Like


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('id', 'name', "created_date", "updated_date")
        read_only_fields = ("created_date", "updated_date")


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    user_id = serializers.IntegerField()

    class Meta:
        model = Like
        fields = ("id", "product", "user", "user_id", "created_date")
        read_only_fields = ("created_date")


class CommentsSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    user_id = serializers.IntegerField()

    class Meta:
        model = Comments
        fields = ("id", "product", "user", "user_id",
                  "comment", "created_date", "updated_date")
        read_only_fields = ("created_date", "updated_date")


class ProductsSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    category_id = serializers.IntegerField()
    like = serializers.SerializerMethodField()
    comment = serializers.SerializerMethodField()

    class Meta:
        model = Products
        fields = ("id", "category", "category_id",
                  "name", "description", "price", "image", "stock", "size", "amount", "like", "comment", "created_date", "updated_date")
        read_only_fields = ("created_date", "updated_date",
                            "category", "category_id")

        def get_like(self, obj):
            return Like.objects.filter(product=obj.id).count()

        def get_comment(self, obj):
            return Comments.objects.filter(product=obj.id).count()
