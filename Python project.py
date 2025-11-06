import datetime
import random

# Restaurants and Menu
restaurants = {
    "1": {
        "name": "Domino's Pizza",
        "menu": {
            "1": ("Margherita Pizza", 249),
            "2": ("Cheese Burst Pizza", 329),
            "3": ("Veggie Paradise", 299),
            "4": ("Peppy Paneer", 319),
            "5": ("Garlic Breadsticks", 119),
            "6": ("Choco Lava Cake", 99),
            "7": ("Pepsi", 60),
            "8": ("Veg Loaded Pizza", 279),
            "9": ("Corn & Cheese Pizza", 289),
            "10": ("Deluxe Veggie Pizza", 339)
        }
    },
    "2": {
        "name": "McDonald's",
        "menu": {
            "1": ("McAloo Tikki Burger", 75),
            "2": ("McSpicy Paneer Burger", 160),
            "3": ("Chicken Maharaja Mac", 210),
            "4": ("Veg Pizza McPuff", 65),
            "5": ("French Fries", 95),
            "6": ("McChicken Burger", 175),
            "7": ("Filet-O-Fish", 190),
            "8": ("Veg Wrap", 130),
            "9": ("McFlurry Oreo", 120),
            "10": ("Coke (Medium)", 70)
        }
    },
    "3": {
        "name": "Saravana Bhavan",
        "menu": {
            "1": ("Idli (2 pcs)", 50),
            "2": ("Vada (2 pcs)", 60),
            "3": ("Dosa", 80),
            "4": ("Poori Masala", 90),
            "5": ("Meals Combo", 180),
            "6": ("Mini Tiffin", 150),
            "7": ("Curd Rice", 100),
            "8": ("Upma", 70),
            "9": ("Chapati with Kurma", 120),
            "10": ("Filter Coffee", 40)
        }
    },
    "4": {
        "name": "KFC",
        "menu": {
            "1": ("Zinger Burger", 190),
            "2": ("Popcorn Chicken", 160),
            "3": ("Chicken Bucket", 450),
            "4": ("French Fries", 90),
            "5": ("Krusher", 110),
            "6": ("Smoky Grilled Chicken", 220),
            "7": ("Hot Wings", 150),
            "8": ("Rice Bowl", 180),
            "9": ("Veg Zinger", 170),
            "10": ("Soft Drink", 60)
        }
    },
    "5": {
        "name": "A2B (Adyar Ananda Bhavan)",
        "menu": {
            "1": ("Mini Tiffin", 150),
            "2": ("South Indian Meals", 180),
            "3": ("Chole Bhature", 140),
            "4": ("Rava Dosa", 110),
            "5": ("Poori Masala", 100),
            "6": ("Paneer Butter Masala", 210),
            "7": ("Ghee Roast Dosa", 130),
            "8": ("Curd Rice", 90),
            "9": ("Kesari Bath", 70),
            "10": ("Filter Coffee", 45)
        }
    },
    "6": {
        "name": "Subway",
        "menu": {
            "1": ("Veggie Delight Sub", 180),
            "2": ("Paneer Tikka Sub", 200),
            "3": ("Chicken Teriyaki Sub", 240),
            "4": ("Tuna Sub", 260),
            "5": ("Italian B.M.T Sub", 280),
            "6": ("Cold Coffee", 120),
            "7": ("Cookies (2 pcs)", 90),
            "8": ("Soft Drink", 60),
            "9": ("Salad Bowl", 160),
            "10": ("Egg & Cheese Sub", 220)
        }
    },
    "7": {
        "name": "Starbucks",
        "menu": {
            "1": ("Cappuccino", 180),
            "2": ("Cafe Latte", 200),
            "3": ("Mocha", 210),
            "4": ("Espresso", 150),
            "5": ("Cold Coffee", 190),
            "6": ("Chocolate Croissant", 140),
            "7": ("Blueberry Muffin", 160),
            "8": ("Brownie", 170),
            "9": ("Strawberry Frappuccino", 230),
            "10": ("Iced Americano", 170)
        }
    },
    "8": {
        "name": "SS Hyderabadi",
        "menu": {
            "1": ("Hyderabadi Chicken Biryani", 260),
            "2": ("Hyderabadi Mutton Biryani", 300),
            "3": ("Veg Biryani", 200),
            "4": ("Egg Biryani", 220),
            "5": ("Paneer Biryani", 240),
            "6": ("Chicken 65", 180),
            "7": ("Raita", 40),
            "8": ("Mirchi ka Salan", 50),
            "9": ("Gulab Jamun", 70),
            "10": ("Soft Drink", 60)
        }
    },
    "9": {
        "name": "Dindigul Thalappakatti",
        "menu": {
            "1": ("Dindigul Mutton Biryani", 320),
            "2": ("Chicken Biryani", 260),
            "3": ("Egg Biryani", 220),
            "4": ("Veg Biryani", 190),
            "5": ("Chicken 65", 180),
            "6": ("Mutton Sukka", 290),
            "7": ("Naatu Kozhi Gravy", 270),
            "8": ("Parotta (2 pcs)", 90),
            "9": ("Onion Raita", 40),
            "10": ("Gulab Jamun", 70)
        }
    }
}

CGST = 0.025
SGST = 0.025

delivery_people = [
    {"name": "Sooraj", "phone": "9566812995"},
    {"name": "Jegan", "phone": "8667465647"},
    {"name": "Haricharan", "phone": "8281773691"},
    {"name": "Vandit", "phone": "7862931393"},
    {"name": "Abinivesh", "phone": "6385448775"}
]


#Home
print("\nWelcome to FoodieExpress – Eat Fresh, Eat Fast!\n")

user_name = input("Enter your name: ").strip().title()

print(f"\nHi {user_name}! Choose your favourite restaurant:\n")
for key, rest in restaurants.items():
    print(f"{key}. {rest['name']}")

rest_choice = input("\nEnter the restaurant number: ")

if rest_choice not in restaurants:
    print("Invalid choice. Please restart.")
    exit()

restaurant = restaurants[rest_choice]
menu = restaurant["menu"]

print(f"\n You selected: {restaurant['name']}")
print("\n---------- MENU ----------")
for key, (item, price) in menu.items():
    print(f"{key}. {item} - ₹{price}")

# Ordering
order = {}
while True:
    choice = input("\nEnter item number (Enter 'ORDER' to finish): ")
    if choice.lower() == "order":
        break
    if choice not in menu:
        print("Invalid item number.")
        continue
    quantity = int(input("Enter quantity: "))
    item_name, item_price = menu[choice]
    order[item_name] = order.get(item_name, 0) + quantity

if not order:
    print("No items ordered. Exiting.")
    exit()


# Bill Calculation
subtotal = sum(
    next(price for num, (name, price) in menu.items() if name == item) * qty
    for item, qty in order.items()
)
cgst = subtotal * CGST
sgst = subtotal * SGST
gst_total = cgst + sgst

# Apply discount
if subtotal >= 1000:
    discount = subtotal * 0.10
elif subtotal >= 500:
    discount = subtotal * 0.05
else:
    discount = 0

grand_total = subtotal + gst_total - discount
delivery_person = random.choice(delivery_people)

# Print Receipt
print("\n---------------------- BILL RECEIPT ----------------------")
print(f"Customer Name: {user_name}")
print(f"Restaurant: {restaurant['name']}")
print(f"Date: {datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n")

print("Items Ordered:")
for item, qty in order.items():
    price = next(price for num, (name, price) in menu.items() if name == item)
    print(f"  {item} x{qty} = ₹{price * qty}")

print("\nSubtotal: ₹{:.2f}".format(subtotal))
print("CGST (2.5%): ₹{:.2f}".format(cgst))
print("SGST (2.5%): ₹{:.2f}".format(sgst))
print("Discount: ₹{:.2f}".format(discount))
print("------------------------------------------------------------")
print("Grand Total: ₹{:.2f}".format(grand_total))
print("------------------------------------------------------------")
print(f"‍Delivery Person: {delivery_person['name']}")
print(f"Contact: {delivery_person['phone']}")
print("\nThank you for ordering with FoodieExpress,", user_name, "! Enjoy your meal \n")
print("Your delivery partner will contact you soon!")
