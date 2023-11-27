"""
* Author: "Tommy McGee(tommymcgee@disroot.org)
*
* License: SPDX-License-Identifier: GPL-3.0-or-later
*
* These are the url paths used for the flava_flav icecream truck assignment
* for zookeep, this will import the views that are used as well
"""
from django.urls import path
from .views import BuyFoodView, InventoryView, EarningsView, CustomerView

urlpatterns = [
    path('buy/', BuyFoodView.as_view(), name='buy-food'),
    path('inventory/', InventoryView.as_view(), name='inventory'),
    path('earnings/', EarningsView.as_view(), name='earnings'),
    path('customers/', CustomerView.as_view(), name='customers'),
]
