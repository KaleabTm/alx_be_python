# shopping_list_manager.py

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
        choice = input("Enter your choice (1-4): ")

        # Validate that choice is a number
        if not choice.isdigit() or not (1 <= int(choice) <= 4):
            print("Invalid choice. Please enter a number between 1 and 4.")
            continue
        
        choice = int(choice)  # Convert choice to an integer
        
        if choice == 1:
            # Prompt for and add an item
            item = input("Enter the item you want to add: ")
            shopping_list.append(item)
            print(f"'{item}' has been added to the shopping list.")
        elif choice == 2:
            # Prompt for and remove an item
            item = input("Enter the item you want to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the shopping list.")
            else:
                print(f"'{item}' not found in the shopping list.")
        elif choice == 3:
            # Display the shopping list
            if shopping_list:
                print("Current Shopping List:")
                for index, item in enumerate(shopping_list, start=1):
                    print(f"{index}. {item}")
            else:
                print("The shopping list is empty.")
        elif choice == 4:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
