from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
)

from .serializers import *
from .models import *



class Home(APIView):

    def get(self, request):
        customers = Customer.objects.all()
        orders = Order.objects.all()

        total_orders = orders.count()

        delivered = orders.filter(status='Delivered').count()
        pending = orders.filter(status='Pending').count()

        s_orders = OrderSerializer(orders, many=True)
        s_customers = CustomerSerializer(customers, many=True)
        
        context =  {'Orders':s_orders.data,'Customers':s_customers.data,
        'total_orders':total_orders,'delivered':delivered,'pending':pending
        }
              
        return Response(context)


class ProductView(APIView):

    def get(self, request):
        products = Product.objects.all()
        s_products = ProductSerializer(products, many=True)
        return Response(s_products.data)


class CustomerView(APIView):

    def get(self, request, pk):
        customer = Customer.objects.get(pk=pk)
        orders = customer.order_set.all()
        order_count = orders.count()

        s_customer = CustomerSerializer(customer)
        s_orders = OrderSerializer(orders, many=True)

        context =  {'Customers':s_customer.data,
        'Orders':s_orders.data,"order_count":order_count
        }
              
        return Response(context)

class OrderView(APIView):
    
    def post(self, request):
        s_order =  OrderSerializer(data = request.data, context={"request": request})
        if s_order.is_valid():
            s_order.save()
            return Response(s_order.data, status=HTTP_201_CREATED)
        return Response(s_order.errors, status=HTTP_400_BAD_REQUEST)