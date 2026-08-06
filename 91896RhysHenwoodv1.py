# List of menu options
menu = [
    "1. Record a speeding offence",
    "2. View all recorded offences",
    "3. Search offence records",
    "4. Display patrol summary",
    "5. Exit Program"
    "6. test"
]

# Dictionary for menu choices
menu_options = {
    "1": "Record a speeding offence",
    "2": "View all recorded offences",
    "3": "Search offence records",
    "4": "Display patrol summary",
    "5": "Exit Program"
}

#function to display menu.
def display_menu():
    print("\n===== Speeding Offence System =====")
    for option in menu:
        print(option)

# Main Program
while True:
    display_menu()
    choice=input("\nEnter your choice (1-5): ")
    
    if choice in menu_options:
        if choice == "5":
            print("exiting program...")
            break
        else:
            print("Invalid choice. Pleas enter a number between 1 and 5.")