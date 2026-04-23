def validate_order(order_type, price):

    if order_type == "LIMIT" and price is None:
        raise ValueError("LIMIT order requires price")

    return True