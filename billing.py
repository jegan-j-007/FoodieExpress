# billing.py
import datetime
import random
import data  # import module to access delivery_people safely



CGST = 0.025
SGST = 0.025

def calculate_bill(menu, order):
    """
    Returns (subtotal, cgst, sgst, discount, grand_total)
    """
    subtotal = sum(
        next(price for num, (name, price) in menu.items() if name == item) * qty
        for item, qty in order.items()
    )
    cgst = subtotal * CGST
    sgst = subtotal * SGST

    # discount rules (unchanged)
    if subtotal >= 1000:
        discount = subtotal * 0.10
    elif subtotal >= 500:
        discount = subtotal * 0.05
    else:
        discount = 0

    grand_total = subtotal + cgst + sgst - discount
    return subtotal, cgst, sgst, discount, grand_total

def print_receipt(user_name, restaurant, menu, order, subtotal, cgst, sgst, discount, grand_total):
    delivery_person = random.choice(data.delivery_people)
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
    print(f"Delivery Person: {delivery_person['name']}")
    print(f"Contact: {delivery_person['phone']}")
    print(f"\nThank you for ordering with FoodieExpress, {user_name}! Enjoy your meal 🍽️\n")

def print_summary(order_history):
    """
    order_history is a list of dicts with keys:
      restaurant, items(dict), subtotal, gst_total, discount, grand_total
    """
    if not order_history:
        print("\nNo orders were placed.\n")
        return

    print("\n==================== ORDER SUMMARY ====================")
    total_spent = 0.0
    total_discount = 0.0
    total_gst = 0.0

    for i, o in enumerate(order_history, 1):
        print(f"\nOrder #{i} - {o['restaurant']}")
        # show items if stored
        if 'items' in o and o['items']:
            items_str = ", ".join(f"{k} x{v}" for k, v in o['items'].items())
            print(f"  Items: {items_str}")
        print(f"  Subtotal: ₹{o['subtotal']:.2f}")
        print(f"  GST: ₹{o['gst_total']:.2f}")
        print(f"  Discount: ₹{o['discount']:.2f}")
        print(f"  Grand Total: ₹{o['grand_total']:.2f}")
        total_spent += o['grand_total']
        total_discount += o['discount']
        total_gst += o['gst_total']

    print("\n------------------------------------------------------------")
    print(f"Total Orders: {len(order_history)}")
    print(f"Total GST Paid: ₹{total_gst:.2f}")
    print(f"Total Discount Received: ₹{total_discount:.2f}")
    print(f"Total Amount Spent: ₹{total_spent:.2f}")
    print("============================================================\n")
