# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 00:51:18 2024

@author: darel
"""

# Dictionary representing items and their prices
motorcycles = {
    "CBR 550": 15000,
    "Ducati Pingiale": 30000,
    "Yamaha R1": 25000,
    "Kawasaki Ninja H2": 56000,
    "BMW G 310 RR ": 23000,
    "Aprilia RS 660": 19000,
    "TVS Apache RTR 160":18500,
    "Honda CBR 600rr":22000,
    "Bajaj Pulsar RS200":18500,
    "Suzuki GSX-R1000R":21500,
    "Benelli 600 RR":17000,
    "Triumph Daytona 675":15500,
    "Harley-Davidson Sportster S":46000,
    "Dodge Tomahawk V10 Superbike":550000,
    "Ecosse ES1 Spirit":3600000,
    "Husqvarna FC 450":12000,
    "Bullet 350":13000,
    "Hero Xtreme 200S 4V":14550,
    'Yamaha FZ 25':13500,
    "Kawasaki Ninja 400":17800,
    "Yamaha Sniper 155 ":5500
}

# Global variables
balance = 0
def display_items():
    print("Available motorcycles:")
    for item, price in motorcycles.items():
        print(f"{item}: ${price}")
def insert_money():
    global balance
    amount = int(input("Insert money (in dollars): "))
    balance += amount
    print(f"Balance: ${balance}")
def select_item():
    display_items()
    item = input("Select a motorcycle: ")
    return item
def vending_machine():
    global balance
    print("Welcome to Vending Moto")
    while True:
        print("\nOptions:")
        print("1. Insert Money")
        print("2. Select Motorcycle")
        print("3. Leave Motorcycle Vending Machine")
        choice = int(input("Enter your choice (1-3): "))
        if choice == 1:
            insert_money()
        elif choice == 2:
            item = select_item()
            if item in motorcycles:
                price = motorcycles[item]
                if balance >= price:
                    print(f"You've purchased a {item} for ${price}. enjoy with your brand new ride!")
                    balance -= price
                    print(f"Remaining balance: ${balance}")
                else:
                    print("Insufficient funds. Please insert more funds.")
            else:
                print("Invalid selection. Please choose a motorcycle from the list.")
        elif choice == 3:
            print("We are honored to serve you. Have a wonderful ride!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    vending_machine()
1