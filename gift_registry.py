"""
Program: Gift Registry
Author: Hannah Rogers
Purpose: Allows users to create and manage a gift registry by adding,
viewing, marking, and removing gifts.
Resources: No starter code was used.
Date: September 26, 2026
"""


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
    gift_price = float(input("Enter the gift price: $"))

    gift = {
        "name": gift_name,
        "price": gift_price,
        "purchased": False
    }
    gifts.append(gift)
    print(gift_name, "was added for $", gift_price)


gifts = []
print("Welcome to the Gift Registry!")

while True:
    show_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        add_gift()   

        
    elif choice == "2":
        if len(gifts) == 0:
            print("Your gift registry is empty.")
        else:
            for gift in gifts:
                if gift["purchased"] == True:
                    print(gift["name"], "-", "$", gift["price"], "- Purchased")
                else:
                    print(gift["name"], "-", "$", gift["price"], "- Not Purchased")

    elif choice == "3":
        gift_name = input("Enter the name of the gift that was purchased: ")
        found = False

        for gift in gifts:
            if gift["name"] == gift_name:
                gift["purchased"] = True
                print(gift_name, "has been marked as purchased!")
                found = True
                break

        if found == False:
            print("Gift not found in the registry.")
    
    elif choice == "4":
            gift_name = input("Enter the name of the gift you'd like to remove: ")
            found = False

            for gift in gifts:
                if gift["name"] == gift_name:
                 gifts.remove(gift)
                 print(gift_name, "has been removed from the registry.")
                 found = True
                 break

            if found == False:
                print("Gift not found in the registry.")
    
    elif choice == "5":
        print("Thank you for using the Gift Registry!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")