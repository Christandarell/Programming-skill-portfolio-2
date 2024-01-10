# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 07:34:52 2024

@author: darel
"""


# Dictionary representing items, their IDs, and prices
motorcycles = {
    1: {"name": "Harley Davidson", "price": 15000},
    2: {"name": "Honda CBR", "price": 45500},
    3: {"name": "Yamaha R1", "price": 32000},
    4: {"name": "Kawasaki Ninja H2", "price": 56000},
    5: {"name": "BMW G 310 RR", "price": 34000},
    6: {"name": "Aprilia RS 660", "price": 22000},
    7: {"name": "TVS Apache RTR 160", "price": 15000},
    8: {"name": "Bajaj Pulsar RS200", "price": 13400},
    9: {"name": "Suzuki GSX-R1000R", "price": 21500},
    10: {"name": "Benelli 600 RR", "price": 17000},
    11: {"name": "Triumph Daytona 675", "price": 15500},
    12: {"name": "Dodge Tomahawk V10 Superbike", "price": 550000},
    13: {"name": "Ecosse ES1 Spirit", "price": 3600000},
    14: {"name": "Husqvarna FC 450", "price": 12000},
    15: {"name": "Bullet 350", "price": 13000},
    16: {"name": "Hero Xtreme 200S 4V", "price": 14500},
    17: {"name": "Yamaha FZ 25", "price": 13500},
    18: {"name": "Kawasaki Ninja 400", "price": 17800},
    19: {"name": "Yamaha Sniper 155", "price": 5500},
    20: {"name": "Ducati Pingiale", "price": 30000 },
    



}

# All variables
balance = 0
purchased_items = []

def display_items():
    print("Available motorcycles:")
    for item_id, info in motorcycles.items():
        print(f"{item_id}. {info['name']}: ${info['price']}")

def insert_money():
    global balance
    amount = int(input("Insert money (in dollars): "))
    balance += amount
    print(f"Balance: ${balance}")

def select_item():
    display_items()
    item_id = int(input("Enter the item ID to select a motorcycle: "))
    return item_id

def print_receipt(item_info):
    print("\nReceipt:")
    print(f"Item: {item_info['name']}")
    print(f"Price: ${item_info['price']}")
    print(f"Total: ${sum(item['price'] for item in purchased_items)}")

def vending_machine():
    global balance
    global purchased_items
    
    print("Welcome to MotoV How may i serve you with our motorcycle vending Machine!")
    
    while True:
        print("\nOptions:")
        print("1. Insert Money")
        print("2. Select Motorcycle")
        print("3. Print Receipt")
        print("4. Leave")
        
        choice = int(input("Enter your choice (1-4): "))
        
        if choice == 1:
            insert_money()
        elif choice == 2:
            item_id = select_item()
            if item_id in motorcycles:
                item_info = motorcycles[item_id]
                price = item_info["price"]
                if balance >= price:
                    print(f"You've purchased a {item_info['name']} for ${price}. Enjoy your ride!")
                    purchased_items.append(item_info)
                    balance -= price
                    print(f"Remaining balance: ${balance}")
                else:
                    print("Insufficient funds. Please insert more money.")
            else:
                print("Not Available. Please choose a motorcycle from the list.")
        elif choice == 3:
            if purchased_items:
                for item_info in purchased_items:
                    print_receipt(item_info)
            else:
                print("Please purchase a product first.")
        elif choice == 4:
            print("it's our pleasure to serve you, Thank you for using MotoV Vending Machine. Have a great day!")
            break
        else:
            print("Not Available. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    vending_machine()
