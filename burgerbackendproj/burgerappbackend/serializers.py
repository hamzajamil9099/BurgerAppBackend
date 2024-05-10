# serializers.py
from rest_framework import serializers
from burgerappbackend.models import CustomUser, Order

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(email=validated_data['email'], password=validated_data['password'])
        return user


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['name', 'street', 'zipCode', 'country', 'email', 'deliveryOption', 'lettuce', 'bacon', 'cheese', 'meat', 'total']