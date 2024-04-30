from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework import generics
from .models import HistoricalPerformance, Vendor, PurchaseOrder
from .serializers import HistoricalSerializer, SignUpSerializer, VendorSerializer, PurchaseOrderSerializer
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import SignUpSerializer
from .tokens import create_jwt_pair_for_user
from rest_framework.permissions import IsAuthenticated, AllowAny    
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import HttpResponse, JsonResponse
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.response import Response
import secrets
import requests
class VendorListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = []
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = []
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class PurchaseOrderListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = []
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = []
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class VendorPerformanceAPIView(generics.RetrieveAPIView):
    permission_classes = []
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalSerializer

    def retrieve(self, request, *args, **kwargs):
        vendor_id = self.kwargs.get('vendor_id')
        vendor = get_object_or_404(Vendor, vendor_id=vendor_id)
        performance_metrics = HistoricalPerformance.objects.filter(vendor=vendor)
        serializer = self.get_serializer(performance_metrics, many=True)
        return Response(serializer.data)
    
class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer
    # authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request: Request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            response = {"message": "User Created Successfully", "data": serializer.data}

            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated] 

    def post(self, request: Request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(username=email, password=password)
        
        if user is not None:

            tokens = create_jwt_pair_for_user(user)

            response = {"message": "Login Successfull", "tokens": tokens}
            return Response(data=response, status=status.HTTP_200_OK)

        else:
            return Response(data={"message": "Invalid email or password"})

    def get(self, request: Request):
        content = {"user": str(request.user), "auth": str(request.auth)}

        return Response(data=content, status=status.HTTP_200_OK)