"""
Program: Gift Registry
Author: Hannah Rogers
Purpose: Allows users to create and manage a gift registry by adding,
viewing, marking, and removing gifts.
Resources: No starter code was used.
Date: September 26, 2026
"""

import json
from gift import Gift


def save_gifts():
    """Save all gifts to a JSON file."""
    gift_data = []

    for gift in gifts:
        gift_data.append(gift.to_dict())

    with open("gifts.json", "w") as file:
        json.dump(gift_data, file, indent=4)


def load_gifts():
    """Load gifts from a JSON file."""
    try:
        with open("gifts.json", "r") as file:
            gift_data = json.load(file)

        for item in gift_data:
            gift = Gift(item["name"], item["price"])
            gift.purchased = item["purchased"]
            gifts.append(gift)

    except FileNotFoundError:
        pass



def show_menu():
    """Display the Gift Registry menu."""
    print("1. Add a gift")
    print("2. View gift registry")
    print("3. Mark a gift as purchased")
    print("4. Remove a gift")
    print("5. Exit")

def add_gift():
    """Add a new gift to the registry."""
    gift_name = input("Enter the name of the gift: ")
    try:
        gift_price = float(input("Enter the gift price: $"))
    except ValueError:
        print("Invalid price. Please enter a number.")
        return

    gift = Gift(gift_name, gift_price)
    gifts.append(gift)
    print(gift_name, "was added for $", gift_price)

def view_gifts():
    """Display all gifts in the registry."""
    if len(gifts) == 0:
        print("Your gift registry is empty.")
    else:      
        for gift in gifts:
            if gift.purchased == True:
                print(gift.name, "-", "$", gift.price, "- Purchased")
            else:
                print(gift.name, "-", "$", gift.price, "- Not Purchased")

def mark_purchased():
    """Mark a gift as purchased."""
    gift_name = input("Enter the name of the gift that was purchased: ")
    found = False

    for gift in gifts:
        if gift.name == gift_name:
            gift.purchased = True
            print(gift_name, "has been marked as purchased!")
            found = True
            break

    if found == False:
        print("Gift not found in the registry.")

def remove_gift():
    """Remove a gift from the registry."""
    gift_name = input("Enter the name of the gift you'd like to remove: ")
    found = False

    for gift in gifts:
        if gift.name == gift_name:
            gifts.remove(gift)
            print(gift_name, "has been removed from the registry.")
            found = True
            break

    if found == False:
        print("Gift not found in the registry.")


gifts = []
print("Welcome to the Gift Registry!")


load_gifts()

while True:
    show_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        add_gift()
        save_gifts()
        
    elif choice == "2":
        view_gifts()


    elif choice == "3":
        mark_purchased()
        save_gifts()
    
    elif choice == "4":
        remove_gift()
        save_gifts()
    
    elif choice == "5":
        print("Thank you for using the Gift Registry!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")