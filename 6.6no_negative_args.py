#1. Value error	•	Error: ValueError
#message: price cannot be negative
#line 21
# because of the if price < 0: raise valueerror.
#2. Error: Quantity cannot be negative
#3. What you see: price error
#4. What you don't see: quantity error, because it never gets reached.


def main():
    item_price = -2.99
    quantity = -3
    print(f"{quantity} items at ${item_price} each is:")
    print(f"${calc_subtotal(item_price, quantity)}")


def calc_subtotal(price: float, quantity: int) -> float:
    """Calculate the subtotal for a single item in a cart.
    
    Args:
        price: The price of a single item.
        quantity: Number of a particular item in the cart.

    Returns:
        The subtotal
    """
    if price < 0:
        raise ValueError("Price cannot be negative.")
    if quantity < 0:
        raise ValueError("Quantity cannot be negative.")

    return price * quantity


if __name__ == "__main__":
    main()
