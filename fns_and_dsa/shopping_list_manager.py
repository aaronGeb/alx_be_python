#!/usr/bin/env python3
"""Shopping List Manager"""


def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            items = input("Enter the item you want to add: ")
            shopping_list.append(items)
            print(f"Added '{items}' to the shopping list.")

        elif choice == "2":
            item_to_remove = input("Enter the item you want to remove: ")
            if item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove)
                print(f"Removed '{item_to_remove}' from the shopping list.")
            else:
                print(f"'{item_to_remove}' is not in the shopping list.")
        elif choice == "3":
            if shopping_list:
                print("Shopping List:")
                for item in shopping_list:
                    print(f"- {item}")
            else:
                print("Your shopping list is empty.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
