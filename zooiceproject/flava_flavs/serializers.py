"""
* Author: "Tommy McGee(tommymcgee@disroot.org)
*
* License: SPDX-License-Identifier: GPL-3.0-or-later
*
* These are the serialzers used for the flava_flav icecream truck assignment
* for zookeep, this will import the models that are used as well.
* A self-note Serializers allow complex data such as querysets and model
* instances to be converted to native Python datatypes that can then be easily
* rendered into JSON, XML or other content types
"""

from rest_framework import serializers
from .models import FoodItem, Customer, Transaction

class FoodItemSerializer(serializers.ModelSerializer):
    """ Used with the Fooditem Model """
    class Meta:
        """ The model using all its fields """
        model = FoodItem
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    """ Used with the Customer Model """
    class Meta:
        """ The model using all its fields """
        model = Customer
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    """ Used with the Transaction Model """
    class Meta:
        """ The model using all its fields """
        model = Transaction
        fields = '__all__'
