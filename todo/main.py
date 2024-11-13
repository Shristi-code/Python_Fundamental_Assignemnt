# main.py
from todo_operations import add_task, delete_task, view_tasks
from utils import clear_screen, get_user_input

def display_menu():
    """Display the main menu for the to-do app."""
    print("\nTo-Do List Menu:")
    print("1. Add a new to-do item")
    print("2. View all to-do items")
    print("3. Delete an item by its index")
    print("4. Exit")

def main():
    """Main function to run the to-do list application."""
    while True:
        clear_screen()
        display_menu()
        
        choice = get_user_input("\nEnter your choice (1-4): ")

        if choice == "1":
            task = get_user_input("Enter the new task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
            get_user_input("\nPress Enter to continue...")
        elif choice == "3":
            try:
                index = int(get_user_input("Enter the index of the task to delete: "))
                delete_task(index)
            except ValueError:
                print("Please enter a valid index.")
            get_user_input("\nPress Enter to continue...")
        elif choice == "4":
            print("Exiting the to-do list application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
            get_user_input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
