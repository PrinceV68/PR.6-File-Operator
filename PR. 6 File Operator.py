import os
import datetime
file = input("Ener Your File name Do you want to create (with.txt)")

ch = 0

while ch != 5:
    
    print("Welcome to Personsal Journal manager !")
    
    print("Please Select an Option :- ")

    print("\n1. Add a new Entry ")
    print("2. View All Entries ")
    print("3. Search For an Entry ")
    print("4. Delete All Entries")
    print("5. Exit")
    
    try:
        choice = int(input("\nUser Input: "))
    except ValueError:
        print("\nInvalid input. Please enter a number from 1 to 5.")
        continue
    if choice == 1:
        E_entry = input("Enter Your Entry :- \n")
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(file, "a") as f:
            f.write(f"[{timestamp}]\n{E_entry}\n\n")

        print("Entry Added Successfully")
        
    elif choice == 2:
        if os.path.exists(file):       
            print("Your Journal Entries :- ")
            print("-"*50)
            with open(file,"r") as f:
                print(f.read())

        else:
            print("-" * 50)
            print("No Entries Found . Journal is Currently Empty")
            
    elif choice == 3:
        keyword = input("Enter the text to search :- ")
        found = False

        for line in open(file):
            if keyword in line:
                print(line.strip())
                found = True
        if not found:
            print("No matching entry found.")            
                            
    elif choice == 4:
        if os.path.exists(file):
            os.remove(file)
            print("All entries deleted successfully.")
        else:
            print("Journal is already empty.")
    
    elif choice == 5:
        print("Exiting... Goodbye!")
        break

    else:
        print("Please select a valid option (1-5).")        