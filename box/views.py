from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.db import transaction
from .models import Box, Product, Order
from .serializers import (
    BoxSerializers,
    ProductSerializers,
    OrderSerializer
)
from .services import findPerfactBox


class BoxView(APIView):

    def get(self, request):
        box = Box.objects.all()
        serializer = BoxSerializers(box,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BoxSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class ProductView(APIView):

    def get(self, request):
        product = Product.objects.all()
        serializer = ProductSerializers(product,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class OrderCreateView(APIView):

    def get(self, request):
        order = Order.objects.all().prefetch_related("items__product")
        serializer = OrderSerializer(order,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    @transaction.atomic
    def post(self, request):
        serializer = OrderSerializer(data=request.data)

        if serializer.is_valid():
            order = serializer.save()
            serializer = OrderSerializer(order)
            return Response(serializer.data,status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class RecommendBoxView(APIView):

    def get(self, request, id):
        try:
            order = Order.objects.get(id=id)
        except Order.DoesNotExist:
            return Response({"error": "Order not found"},status=status.HTTP_404_NOT_FOUND)

        box = findPerfactBox(order)
        if "error" in box:
            return Response(box,status=status.HTTP_400_BAD_REQUEST)

        return Response(box,status=status.HTTP_200_OK)