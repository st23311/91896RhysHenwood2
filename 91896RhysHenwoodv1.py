# List of menu options
#a list is yused to store all of the options that will be displayed to the user when the main menu is shown 
menu = [
    "1. Record a speeding offence",
    "2. View all recorded offences",
    "3. Search offence records",
    "4. Display patrol summary",
    "5. Exit Program"
]

# Dictionary for menu options
#this dicotionary stores each menu as a key and the descrition of the option ias its value and makes it easy to check whether the user's menu choise is a valid option
menu_options = {
    "1": "Record a speeding offence",
    "2": "View all recorded offences",
    "3": "Search offence records",
    "4": "Display patrol summary",
    "5": "Exit Program"
}
#list to record wanted people
#when an offence is recorded, the driver's name is checekd against this list and if the name is found the program should display a warning.
wanted_people = [
    "Rhys Henwood",
    "Connor Peter Riley",
    "Max Homan",
    "Taylor Hall",
    "John Smith"
]

# List to store recorded offences
#the empty list is used to store all speeding offences recorded during the patrol such as driver's name, licence number, speed limit, recorded speed, amount over and the fine.
offences = []

#function to display menu.
#a for loop is used to go through eveyr iterm in the menu lsit and print it.
def display_menu():
    #print a heading
    print("\n===== Speeding Offence System =====")
    #go through each option in the menu
    for option in menu:
        #display the current menu option
        print(option)
        
#function to get and validate the driver's licnce number and checks that it follows the valid format of "AB123456"
def get_licence_number():
    #keep repeating until a valid licence number is entered.
    while True:
        #
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
        

#fuction to calculate the fine
def calculate_fine(over):
    if over<= 10:
        return 30
    elif over <=20:
        return 80
    elif over <=30:
        return 170
    elif over <=40:
        return 400
    else:
        return 630
    

        
#function to check if the driver is wanted
def check_wanted(driver_name):
    if driver_name in wanted_people:
        print("WARNINGL: This driver is on the wanted lsit!")
        return True
    else:
        print("driver is not on the wanted lsit.:)")
        return False
    
#Function to display all recorded offences    
def view_offences():
    if len(offences) == 0:
        print("\n No recorded offences have occurred")
    else:
        print("\n===== Recorded Offences =====")
        print(f"{'Driver':<20}{'Licence':<12}{'Limit':<8}{'Speed':<8}{'Over':<8}")
        print("-" * 56)
        
        for offence in offences:
            print(f"{offence['Driver']:<20}"
                  f"{offence['Licence']:<12}"
                  f"{offence['Limit']:<8}"
                  f"{offence['Speed']:<8}"
                  f"{offence['Over']:<8}")   
            
#Function to search for an offence 

def search_offences():
    search = input("Enter a driver's full name or licence plate number: ").strip().upper()
    
    found = False 
    
    for offence in offences:
    #Seach 
        if offence["Driver"].upper() == search:
            print("\nOffence found:")
            print("Driver:", offence["Driver"])
            print("Licence:",offence["Licence"])
            print("Speed limit:", offence["Limit"], "km/h")
            print("Recorded Speed limit:",offence["Speed"], "km/h")
            print("Over Limit:",offence["Over"], "km/h")

            found = True
            
            
            #Search by Licence plate number
            
        elif offence["Licence"].upper() == search:
                print("\nOffence found:")
                print("Driver:", offence["Driver"])
                print("Licence:",offence["Licence"])
                print("Speed limit:", offence["Limit"], "km/h")
                print("Recorded Speed limit:",offence["Speed"], "km/h")
                print("Over Limit:",offence["Over"], "km/h")

                found = True
                
            
    if not found:
        print("There are no driver's names or licence number in our offence records")
                

#Function to do patrol summary
def patrol_summary():
    if len(offences) == 0:
        print("\nNo offences has been recorded")
        return 

    #totla number of offences 
    total_offences = len(offences)

    #Total value of offences
    total_fines = 0
    for offence in offences:
        total_fines += offence["Fine"]
    
    #Average amoutnt over the speed limit 
    total_over = 0
    for offence in offences:
        total_over += offence["Over"]
    
        average_over = total_over / total_offences 

        #Find the highest speeder
        highest_offence = offences[0]
        for offence in offences:
            if offence["Over"] > highest_offence["Over"]:
                highest_offence = offence
                #Display patrol summary

                print("\n======Patrol Summary =====")
                print("Total offences recorded:", total_offences)
                print("Total vlaue of infringment fines: $", total_fines)
                print("average speed over the limit:", round(average_over, 1), "km/h")
                print("Highest speeding offence:")
                print("Driver:", highest_offence["Driver"])
                print("Speed over limit:", highest_offence["Over"],"km/h")
# Main Program
while True:
    display_menu()
    choice=input("\nEnter your choice (1-5): ")
    
    if choice in menu_options:

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

                over = recorded_speed - speed_limit
                    
                    #calculate the fine
                fine = calculate_fine(over)
                    
                print("Speed sxceeded by:", over, "km/h")
                print("Infringment fine:$ ", fine)                

                offence = {
                    "Driver": driver_name,
                    "Licence": licence_number,
                    "Limit": speed_limit,
                    "Speed": recorded_speed,
                    "Over": over,
                    "Fine":fine
                }

                offences.append(offence)

                # Check if driver is wanted
                check_wanted(driver_name)

        elif choice == "2":
            view_offences()

        elif choice == "3":
            search_offences()

        elif choice == "4":
            patrol_summary()

        elif choice == "5":
            print("Exiting Program...")
            break

    else:
        print("Invalid choice. Pleas enter a number between 1 and 5.")