# main.py
import data
from ui import show_discounts, choose_restaurant, display_menu
from order import take_order
from billing import calculate_bill, print_receipt, print_summary

def main():
    print("\nWelcome to FoodieExpress – Eat Fresh, Eat Fast!\n")
    show_discounts()
    user_name = input("Enter your name: ").strip().title()

    order_history = []

    while True:
        # Choose restaurant (returns restaurant dict or None)
        restaurant = choose_restaurant(data.restaurants)
        if restaurant is None:
            # invalid choice: ask again
            continue

        display_menu(restaurant["menu"])

        # take_order(menu) returns order dict {item_name: qty} or None
        order_dict = take_order(restaurant["menu"])
        if order_dict is None:
            print("No items ordered. Returning to restaurant selection.\n")
            continue

        # calculate bill
        subtotal, cgst, sgst, discount, grand_total = calculate_bill(restaurant["menu"], order_dict)
        gst_total = cgst + sgst

        # print single order receipt
        print_receipt(user_name, restaurant, restaurant["menu"], order_dict, subtotal, cgst, sgst, discount, grand_total)

        # save to history (store items dict so summary can list them)
        order_history.append({
            "restaurant": restaurant["name"],
            "items": order_dict.copy(),
            "subtotal": subtotal,
            "gst_total": gst_total,
            "discount": discount,
            "grand_total": grand_total
        })

        # Ask whether to place another order
        again = input("\nDo you want to place another order? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            break

    # After user finishes, print overall session summary
    print_summary(order_history)
    print(f" Thanks for using FoodieExpress, {user_name}! Have a great day!\n")

if __name__ == "__main__":
    main()
