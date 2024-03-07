from django.urls import path

from rest_framework_simplejwt import views as jwt_views

from apps.user_auth.api import views

urlpatterns = [
    path("registration/", views.RegisterUserAPIView.as_view(), name="custom_register"),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
