my_list=[]
def create_list():
    my_list=[]
    print("New list created successfully.")

def add_item(item):
    my_list.append(item)
    print(f"'{item}' added to the list.")

def remove_item(item):
    if item in my_list:
        my_list.remove(item)
        print(f" '{item}' removed from the list.")
    else:
        print(f" '{item}' not found in the list.")

def view_list():
    if my_list:
        print("Current List:")
        for index, item in enumerate(my_list,start=1):
            print(f"{index}.{item}")
    else:
        print("The list is empty.")

def copy_list():
    copied_list = my_list.copy()
    print("List copied successfully!")
    print("copied List",copied_list)

def sort_list():
    my_list.sort()
    print("List sorted successfully!")

def list_length():
    print(f" The List contains {len(my_list)} items.")

def clear_list():
    my_list.clear()
    print("List cleared successfully!")

def menu():
    print("\n--- List Manager ---")
    print("1. Create a List")
    print("2. Add Item to List")
    print("3. Remove Item from List")
    print("4. View List")
    print("5. Copy List")
    print("6. Sort List")
    print("7. List Length")
    print("8. Clear List")
    print("9. Exit")


def list_manager():
    while True:
        menu()
        choice = input("Enter your choice(1-9): ")

        if choice == "1":
            create_list()
        elif choice == "2":
            item=input("Enter the item to add:")
            add_item(item)
        elif choice == "3":
            item=input("Enter the remove item:")
            remove_item(item)
        elif choice == "4":
            view_list()
        elif choice == "5":
            copy_list()
        elif choice == "6":
            sort_list()
        elif choice == "7":
            list_length()
        elif choice == "8":
            clear_list()
        elif choice == "9":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    list_manager()