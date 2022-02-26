from django.shortcuts import render
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product

# Create your views here.


class LatestProductsList(APIView):
    def get(self, request):
        products = Product.objects.all()[:10]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
