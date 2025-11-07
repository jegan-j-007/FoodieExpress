# ui.py
from data import restaurants

def show_discounts():
    print("\n🎉 Available Discounts:")
    print("→ 10% off on orders ₹1000 or above")
    print("→ 5% off on orders ₹500 or above")
    print("→ No discount for orders below ₹500\n")

def choose_restaurant(restaurants_dict):
    print("\nChoose your favourite restaurant:\n")
    for key, rest in restaurants_dict.items():
        print(f"{key}. {rest['name']}")
    choice = input("\nEnter the restaurant number: ").strip()
    if choice not in restaurants_dict:
        print("Invalid choice.")
        return None
    return restaurants_dict[choice]

def display_menu(menu):
    print("\n---------- MENU ----------")
    for key, (item, price) in menu.items():
        print(f"{key}. {item} - ₹{price}")
