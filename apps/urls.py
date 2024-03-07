from django.urls import path, include

urlpatterns = [
    path("user-auth/", include("apps.user_auth.api.urls")),
    path("product/", include("apps.product.api.urls")),
]
