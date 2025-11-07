# order.py
def take_order(menu):
    """
    Shows the menu (menu param), accepts item numbers and quantities,
    returns an order dict {item_name: qty}
    """
    order = {}
    while True:
        choice = input("\nEnter item number (Enter 'ORDER' to finish): ").strip()
        if choice.lower() == "order":
            break
        if choice not in menu:
            print("Invalid item number.")
            continue
        try:
            quant = int(input("Enter quantity: ").strip())
            if quant <= 0:
                print("Invalid quantity.")
                continue
        except ValueError:
            print("Invalid quantity.")
            continue
        item_name, item_price = menu[choice]
        order[item_name] = order.get(item_name, 0) + quant

    if not order:
        return None
    return order
