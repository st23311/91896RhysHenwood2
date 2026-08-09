# List of menu options
menu = [
    "1. Record a speeding offence",
    "2. View all recorded offences",
    "3. Search offence records",
    "4. Display patrol summary",
    "5. Exit Program"
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
        
#function to get and validate the driver's licnce number
def get_licence_number():
    while True:
        licence = input("Enter driver's licence number: ").upper()
        if len(licence) ==8:
               if licence[:2].isalpha() and licence[2:].isdigit():
                   return licence
               
               print("Invalid licence number. It must be in the format of AB123456.")

# Main Program
while True:
    display_menu()
    choice=input("\nEnter your choice (1-5): ")
    
    if choice in menu_options:
        if choice == "5":
            print("Exiting Program...")
            break
        else:
            print("You selected:", menu_options[choice])
    else:
        print("Invalid choice. Pleas enter a number between 1 and 5.")