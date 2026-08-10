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

#function to get and validate the driver's full name
def get_driver_name():
    while True:
        name = input("Enter driver's full name: ").strip()

        if name != "":
            return name.title()

        print("Driver's name cannot be blank.")
        
#Function to gert and validate tthe postred speed limit
def get_speed_limit():
    while True:
        speed_limit = input("Enter posted speed limit (30-110 km/h): ")
        
        if speed_limit.isdigit():
            speed_limit = int(speed_limit)
            
            if 30 <= speed_limit <= 110:
                return speed_limit

        print("Invalid speed limit. Enter a whole number between 30 and 110.")
        
#function to get and validate the recoreded speed 
def get_recorded_speed(speed_limit):
    while True:
        recorded_speed = input("Enter recorded speed (km/h): ")

        if recorded_speed.isdigit():
            recorded_speed = int(recorded_speed)

            if recorded_speed > speed_limit:
                return recorded_speed
            else:
                print("No speeding offence occurred.")
                return None

        print("Invalid speed. Enter a whole number.")

# Main Program
while True:
    display_menu()
    choice=input("\nEnter your choice (1-5): ")
    
    if choice in menu_options:
        if choice == "5":
            print("Exiting Program...")
            break
        else:
            if choice == "1":
                driver_name = get_driver_name()
                licence_number = get_licence_number()
                speed_limit = get_speed_limit()
                recorded_speed = get_recorded_speed(speed_limit)
                
                print("Driver Name:", driver_name)
                print("Licence Number:", licence_number)
                print("Posted Speed Limit:", speed_limit, "km/h")
               
                if recorded_speed is not None:
                    print("Recorded Speed:", recorded_speed, "km/h")                
                
    else:
        print("Invalid choice. Pleas enter a number between 1 and 5.")