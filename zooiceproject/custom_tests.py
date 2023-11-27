"""
* Author: "Tommy McGee(tommymcgee@disroot.org)
*
* License: SPDX-License-Identifier: GPL-3.0-or-later
*
* These are the tests that utilize curl to test the API, depending on the
* option that is chosen, it will run the corresponding test.
*
* Option 1 will ask you for addtional input to complete the test.
* Options 2 - 4 will display results or a list of results for viewing purposes
* Further notes **************************************************************
* These tests were written on a Linux operating system however using the
* subprocess module, this should run on Windows or Mac as well. That is also
* why the use of the shlex module. This is particularly useful when dealing
* with command-line interfaces, subprocesses, and other scenarios where we need
* to handle shell-like syntax in a programmatic way, and json is used to display 
* data for ease of reading
"""

import subprocess
import shlex
import json


def test_buy_food_process():
    """  
    First prompt the user for input, then construct the data dictionary,
    convert data dictionary to a string and format it, then make the curl
    command and split the command string into a list, then, execute the curl
    command 
    """
    api_url = "http://localhost:8000/api/buy/"
    customer = input("Enter the customer ID: ")
    food_item = input("Enter the food item ID: ")
    quantity_purchased = input("Enter the quantity purchased: ")
    data = {"customer": customer, "food_item": food_item,
            "quantity_purchased": quantity_purchased
            }
    data_str = "&".join([f"{key}={value}" for key, value in data.items()])
    curl_command = f'curl -X POST {api_url} -d "{data_str}"'
    command_list = shlex.split(curl_command)
    subprocess.run(command_list, shell=False)


def test_earnings():
    """ Simply show the earnings of the truck """
    api_url = "http://localhost:8000/api/earnings/"
    curl_command = f'curl {api_url}'
    command_list = shlex.split(curl_command)
    subprocess.run(command_list, shell=False)


def test_run_api(api_url):
    """
    Run the command and capture the output. Check if the command was successful,
    decode the byte output to a string, load the JSON data, and print the JSON
    data for easy viewing. If there are any problems, show an error message.
    """
    curl_command = f'curl {api_url}'
    command_list = shlex.split(curl_command)
    result = subprocess.run(command_list, shell=False, capture_output=True)
    if result.returncode == 0:
        json_data = result.stdout.decode('utf-8')
        data = json.loads(json_data)
        formatted_data = json.dumps(data, indent=2)
        print(formatted_data)
    else:
        print(f"Error: {result.stderr.decode('utf-8')}")


def test_inventory():
    """ Use the inventory api and run with the test_run_api function"""
    api_url = "http://localhost:8000/api/inventory/"
    test_run_api(api_url)


def test_customer():
    """ Use the customer api and run with the test_run_api function"""
    api_url = "http://localhost:8000/api/customers/"
    test_run_api(api_url)


def main():
    """
    Used as a starting point for the user, to decide what test they would like
    to run for the flava_flavs application.
    """
    print("Choose a test to run:")
    print("1. Buy Food Process")
    print("2. Earnings (Will Show Earnings)")
    print("3. Inventory (List what is in the food item inventory)")
    print("4. Customer (List the customers)")
    user_choice = input("Enter the number of the test you want to run: ")
    if user_choice == "1":
        test_buy_food_process()
    elif user_choice == "2":
        test_earnings()
    elif user_choice == "3":
        test_inventory()
    elif user_choice == "4":
        test_customer()
    else:
        print("Invalid choice. Please enter 1 or 4.")

if __name__ == "__main__":
    main()
