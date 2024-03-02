#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount: int = 0):
        # Initialize the total amount and the list of items
        self.total = 0.0
        self.items = []
        # Initialize the discount percentage
        self.discount = discount

    def add_item(self, title: str, price: float, quantity: int = 1) -> None:
        # Calculating the total price for the item
        total_price = price * quantity
        # To add the total price to the total amount
        self.total += total_price
        # To add the item to the list of items
        self.items.append((title, total_price))

    def apply_discount(self) -> None:
        # Checking if there is a discount to apply
        if self.discount > 0:
            # To calculate the discount amount
            discount_amount = self.total * (self.discount / 100)
            # Subtracting the discount amount from the total amount
            self.total -= discount_amount
            # Printing the total amount after applying the discount
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            # To print a message if there is no discount to apply
            print("There is no discount to apply.")

    def void_last_transaction(self) -> None:
        # Checking if there are any items in the register
        if self.items:
            # Getting the total price of the last item
            last_item_price = self.items[-1][1]
            # To subtract the total price of the last item from the total amount
            self.total -= last_item_price
            # Removing the last item from the list of items
            self.items.pop()

    def get_total(self) -> float:
        # To return the total amount
        return self.total

    def get_items(self) -> list:
        # Returning the list of items
        return self.items

    def reset(self):
        # To reset the total amount and the list of items
        self.total = 0.0
        self.items = []
    pass