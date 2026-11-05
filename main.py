print("Welcome to Python Task Manager!")

def show_menu():
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

tasks = []

while True:

    show_menu()

    choice = input("\nEnter your choice: ")
    if choice == '1':
        print("Add Task Selected")
    elif choice == '2':
        print("View Tasks Selected")
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
