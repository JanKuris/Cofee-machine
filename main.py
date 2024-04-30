from data import MENU, resources

def customer_input():
    customer_choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if customer_choice in ["espresso", "latte", "cappuccino"]:
        return customer_choice
    # elif customer_choice == "report":
    #     print(resources)
    # elif customer_choice == "help":
    #     print("""
    #         Type 'report' for resources status.
    #         Type 'off' for turn off coffe machine.
    #         """) 
    # elif customer_choice == "off":
    #    return "off"    
    
def resources_check(customer_order):
    for ingredient, value in MENU[customer_order]["ingredients"].items():
        if resources[ingredient] < value:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
        resources[ingredient] -= value
    for ingredient, amount in resources.items():
        print(f"{ingredient}: {amount}") 

def coins_calculator(customer_order):
    print(f"Please your drink cost ${MENU[customer_order]['cost']}, insert coin: ")
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickels = int(input("How many nickles: "))
    pennies = int(input("How many pennies: "))
    total_value = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)
    if total_value >= MENU[customer_order]['cost']:
        money_back = total_value - MENU[customer_order]['cost']
        formated_money_back = "{:.2f}".format(money_back)
        print(f"Here is ${formated_money_back} in change")
        print(f"Here is your {customer_order}. Enjoy :)")
        
                  
def main():
    while True:
        customer_order = customer_input()
        if customer_order == "off":
            return False
        elif customer_order == "help":
            print("""Type 'report' for resources status.
                Type 'off' for turn off coffe machine.
                """)
        elif customer_order == "report":
            print(resources)
        # if customer_order == "off":
        #     return False
        resources_check(customer_order)
        coins_calculator(customer_order)
     
    

machine_work = True
while machine_work:
    machine_work = main()

   
    
