from django.urls import path
from .views import LoginView, SignUpView, VendorListCreateAPIView, VendorPerformanceAPIView, VendorRetrieveUpdateDestroyAPIView, PurchaseOrderListCreateAPIView, PurchaseOrderRetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
    path('vendors/', VendorListCreateAPIView.as_view(), name='vendor-list-create'),
    path('vendors/<uuid:pk>/', VendorRetrieveUpdateDestroyAPIView.as_view(), name='vendor-retrieve-update-destroy'),
    path('purchase-orders/', PurchaseOrderListCreateAPIView.as_view(), name='purchase-order-list-create'),
    path('purchase-orders/<uuid:pk>/', PurchaseOrderRetrieveUpdateDestroyAPIView.as_view(), name='purchase-order-retrieve-update-destroy'),
    path('api/vendors/<uuid:vendor_id>/performance/', VendorPerformanceAPIView.as_view(), name='vendor-performance'),
   path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("jwt/create/", TokenObtainPairView.as_view(), name="jwt_create"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
