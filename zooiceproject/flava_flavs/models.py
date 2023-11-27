"""
* Author: "Tommy McGee(tommymcgee@disroot.org)
*
* License: SPDX-License-Identifier: GPL-3.0-or-later
*
* These are the models used for the flava_flav icecream truck assignment 
* for zookeep
"""

from django.db import models

class FoodItem(models.Model):
    """ The inventory model of the food items in the truck"""
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity_in_stock = models.IntegerField()


class Customer(models.Model):
    """ The customers that purchase things from the truck """
    name = models.CharField(max_length=100)


class Transaction(models.Model):
    """ the pruchase events from the truck """
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity_purchased = models.IntegerField()
    purchase_date = models.DateTimeField(auto_now_add=True)
