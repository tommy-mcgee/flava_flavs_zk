# The ZooKeep IceCream truck assignment
## Description:
This is a Django, API project that was given by ZooKeep to assess the understanding of the Django Rest Framework

The API has the following endpoints:
- To buy a specific food from the ice-cream truck
- Give the inventory of the ice-cream truck
- Show the earnings
- Show the customers

What does this project do?
1. It will let a customer purchase food from the ice-cream truck
2. As things are purchased it will update the inventory to reflect what is still available
3. If a purchase qty is out of inventory or exceeds the qty in inventory the result is SORRY!
4. If a purchase qty is available in the inventory or does not exceed the qty in the inventory the result will be ENJOY!
5. Show the Earnings
6. The inventory is listed
7. The customers are listed

The way the testing of the API functions is, that it's all based on IDs this is done for the sake of time and proof of concept. 
For this simple assessment I did not see the need to take any further steps than that.

**For Example**
The custom_tests will ask for a customer ID rather than a customer name, and a food item ID rather than a food_item name.
  

## Stucture details
- Project name: zooiceproject
- App name: flava_flavs

## Base Directory
Along with the standard Django files and folders, I have included a tests file named **custom_tests.py**
This is a testing module that is custom and does not come with the standard Django install. It uses, curl to 
test the APIs. This approach of testing is faster for my workflow on this particular project. 

**Notes:** *this assignment was written and tested on PeppermintOS (Devuan), this should run on any Linux operating system
via pip and ideally if using pip on Windows and Mac environments these steps should run as well. 
This MVP will only take integers for testing, when you go to purchase something*

To use the **custom_tests.py** follow these steps:
*We will make the assumption that Django and the  Django Rest Framework are both installed.*

1. Ensure that your Django development server is running
2. Navigate via terminal to the ```./zooiceproject``` base directory
3. run ```python3 custom_tests.py```
4. The application will prompt you with four options
```
Choose a test to run:
1. Buy Food Process
2. Earnings (Will Show Earnings)
3. Inventory (List what is in the food item inventory)
4. Customer (List the customers)
Enter the number of the test you want to run: 
```
- If you choose option one you will be prompted for a customerid you can enter 1 as the value
- Then you will be prompted for the food item ID you can enter 2 as the value
- Finally you will be prompted for quantity purchased you can enter any value, but in this example you can enter 3
- Result will be SORRY! | this is because the food item 2 is currently a qty of 0 in the inventory, meaning no more are available for purchase

5. You can check what is in the inventory by running the custom_tests module again, choose options three to see the
full inventory list
6. You can do the same for customers to see the full list of what customers you have in the customer model
7. Finally, option 2 will show the Earning for the truck.
