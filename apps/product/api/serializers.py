from rest_framework import serializers

from apps.product.models import *
from apps.user_auth.api.serializers import UserSerializer


class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ListProductSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    merchant = MerchantSerializer()
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "name",
            "quantity",
            "description",
        )
