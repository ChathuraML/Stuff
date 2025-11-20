from menu import menu
from coin import coin
from inventry import inventry

def report():
    print(f"Water : {inventry["water"]}ml")
    print(f"Milk  : {inventry["milk"]}ml")
    print(f"Coffee: {inventry["coffee"]}g")
    print(f"Money : ${inventry["money"]}")


def bill(quarters,dims,nickles,pennies,coffee_type_request):
    cents = 0.25 * float(quarters) + 0.1 * float(dims) + 0.05 * float(nickles) + 0.01 * float(pennies)
    charge = menu[coffee_type_request]["cost"]
    balance = round(cents - charge,2)

    if charge > cents:
        print(f"You need {round(charge - cents,2)} more to have a {coffee_type_request}. Money refunded.")
    else:
        print(f"Here is ${balance} in change")
        print(f"Here is your {coffee_type_request} ☕ enjoy!")

def inventry_update(count, requested_coffe_type):
    if count:
        inventry["water"] = inventry["water"] - menu[requested_coffe_type]["ingredients"]["water"]
        inventry["milk"] = inventry["milk"] - menu[requested_coffe_type]["ingredients"]["milk"]
        inventry["coffee"]= inventry["coffee"] - menu[requested_coffe_type]["ingredients"]["coffee"]
        inventry["money"] = inventry["money"] + menu[requested_coffe_type]["cost"]
    return inventry

def inventry_status(inventry, requested_coffe_type):
    low_items = ""
    for i in inventry:
        if i != "money":
            if inventry[i] - menu[requested_coffe_type]["ingredients"][i] < 0:
                low_items += f"{i} and "
    low_items = low_items.rstrip(" and")
    return low_items     

def machine():
    updating_inventory = False
    new_customer = True
    while new_customer:
        coffee_type_userInput = input("What would you like? (espresso/latte/cappuccino) or (report/off):").lower()
        
        if coffee_type_userInput == "off":
            print("Have nice day!!!")
            new_customer = False
        else:    
            while coffee_type_userInput == "report":
                report()
                coffee_type_userInput = input("What would you like? (espresso/latte/cappuccino):").lower()

            new_invetory = inventry_update(updating_inventory, coffee_type_userInput) 
            low_inventry_item = inventry_status(new_invetory, coffee_type_userInput)
            
            if coffee_type_userInput != "report":
                if low_inventry_item:
                    print(f"Sorry there is not enough {low_inventry_item}.")
                else:   
                    print("Please insert coins.")
                    coin_type_quarter = float(input("How many quarters?: "))
                    coin_type_dims = float(input("How many dims?: "))
                    coin_type_nickles = float(input("How many nickles?: "))
                    coin_type_pennies = float(input("How many pennies?: "))
                    
                    #order(coffee_type_userInput)
                    bill(coin_type_quarter,coin_type_dims,coin_type_nickles,coin_type_pennies,coffee_type_userInput)

                    #updating the inventory
                    updating_inventory = True
                    new_invetory = inventry_update(updating_inventory, coffee_type_userInput)
                    updating_inventory = False
            else:
                new_customer = False
     
machine()