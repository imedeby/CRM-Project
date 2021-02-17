from rest_framework.serializers import ModelSerializer

from .models import *

class CustomerSerializer(ModelSerializer):

    class Meta:
        model = Customer
        fields = "__all__"


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product  
        fields = "__all__"

class TagSerializer(ModelSerializer):

    product = ProductSerializer()

    class Meta:
        model = Tag
        fields = "__all__"


class OrderSerializer(ModelSerializer):

    customer = CustomerSerializer()
    product = ProductSerializer()

    class Meta:
        model = Order
        fields = "__all__"