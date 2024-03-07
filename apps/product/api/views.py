from rest_framework.permissions import AllowAny
from rest_framework import generics

from apps.product.models import *
from apps.product.api.serializers import (
    ListProductSerializer,
    ProductSerializer,
)


class ProductListAPIView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ListProductSerializer

    def get_queryset(self):
        return (
            Product.objects.prefetch_related(
                "hashtags",
                "keywords",
                "merchant__hashtags",
                "merchant__categories",
                "merchant__keywords",
            )
            .select_related(
                "merchant",
                "category",
                "owner",
            )
        )


class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductSerializer


class ProductDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ProductSerializer

    def get_object(self):
        return Product.objects.filter(pk=self.kwargs.get("product_id")).first()
