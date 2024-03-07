from django.urls import path, include

from apps.product.api import views


urlpatterns = [
    path("", views.ProductListAPIView.as_view()),
    path("create/", views.ProductCreateAPIView.as_view()),
    path("<uuid:product_id>/", views.ProductDestroyAPIView.as_view()),
]
