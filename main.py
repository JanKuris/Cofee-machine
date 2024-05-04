from data import MENU, resources, money_vault

def customer_input():
    customer_choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if customer_choice in ["espresso", "latte", "cappuccino"]:
        return customer_choice
    else:
        if customer_choice == "off":
            return False
        elif customer_choice == "help":  
            print("""
                Type 'report' for resources status.
                Type 'off' for turn off coffe machine.
                """)
            return None
        elif customer_choice == "report":
            print(resources)
            sum_money = sum(money_vault)
            print(f"Money: ${sum_money}")
            return None
    return True
    
def resources_check(customer_order):
    for ingredient, value in MENU[customer_order]["ingredients"].items():
        if resources[ingredient] < value:
            print (f"Sorry, there is not enough {ingredient}.")
            return False
        resources[ingredient] -= value
    for ingredient, amount in resources.items():
        res = f"{ingredient}: {amount}"
        return res

def coins_calculator(customer_order):
    print(f"Please your drink cost ${MENU[customer_order]['cost']}, insert coin: ")
    quarters = int(input("How many quarters: ")) 
    dimes = int(input("How many dimes: "))
    nickels = int(input("How many nickles: "))
    pennies = int(input("How many pennies: "))
    total_value = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)
    if total_value < MENU[customer_order]['cost']:
        print("Sorry, that's not enough money. Money refunded.")
        return True
    change = total_value - MENU[customer_order]['cost']
    formated_money_back = "{:.2f}".format(change)
    money_vault.append(MENU[customer_order]['cost'])
    print(f"Here is ${formated_money_back} in change")
    print(f"Here is your {customer_order}. Enjoy :)")
    return True
                  
def main():
    customer_order = customer_input()
    if customer_order is None:
        return True
    elif customer_order == False:
        return False
    elif resources_check(customer_order) and coins_calculator(customer_order):
        return True
    else:
        return False

if __name__ == "__main__":
    while True:
        if not main():
            break
     
