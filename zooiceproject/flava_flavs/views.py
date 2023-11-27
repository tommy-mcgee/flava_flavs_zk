"""
* Author: "Tommy McGee(tommymcgee@disroot.org)
*
* License: SPDX-License-Identifier: GPL-3.0-or-later
*
* These are the views used for the flava_flav icecream truck assignment
* for zookeep, this will import the models that are used as well.
* Also, the Sum aggregation function is used to sum the earnings and F is used
* to reference database columns in queries, allowing me to perform operations
* on the database level.
"""
from django.db.models import Sum, F
from django.shortcuts import render
from rest_framework import generics, status, serializers
from rest_framework.response import Response
from .models import FoodItem, Transaction, Customer
from .serializers import FoodItemSerializer, TransactionSerializer, CustomerSerializer

class BuyFoodView(generics.CreateAPIView):
    """ Used to manage the buying of food actions"""
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def perform_create(self, serializer):
        """ 
        Create the record of what is being purchased, if it goes over the
        the qty listed for the food_item then say SORRY! otherwise say ENJOY!
        """
        food_item = serializer.validated_data['food_item']
        quantity_purchased = serializer.validated_data['quantity_purchased']
        if food_item.quantity_in_stock < quantity_purchased:
            raise serializers.ValidationError("SORRY!")
        food_item.quantity_in_stock -= quantity_purchased
        food_item.save()
        serializer.save()

    def create(self, request, *args, **kwargs):
        """
        Override the default create method to return a success message.
        """
        response = super().create(request, *args, **kwargs)
        return Response({"detail": "ENJOY!"}, status=status.HTTP_201_CREATED)


class InventoryView(generics.ListAPIView):
    """ Used to keep a list of the what is in the inventory """
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer

class CustomerView(generics.ListAPIView):
    """ Used to keep a list of the Customers """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class EarningsView(generics.ListAPIView):
    """ Used to keep a list of the Earnings """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get(self,*args):
        """ 
        Tally up the things purchased, and sum them to get the final 
        earnings made 
        """
        total_earnings = Transaction.objects.aggregate(
            total_earnings=Sum(F('quantity_purchased') * F('food_item__price'))
        )['total_earnings']
        return Response({"total_earnings": total_earnings})
