#====================================================
#        RAILWAY TICKETING MANAGEMENT SYSTEM
#=====================================================



#======================================================
#                 USER MENU 
#======================================================

def user_menu(username):               #Returns the username credentials and proceeds with the within functions
    while True:
        print("\n========================================")
        print("              USER MENU")
        print("=========================================")

        print("Logged in as:", username)
                                         # Catalog associated in Railway Ticketing system
        print("\n1. Book Railway Ticket")
        print("2. View My Bookings")
        print("3. Search Ticket")
        print("4. Cancel Ticket")
        print("5. Logout")

        choice = input("\nEnter your choice:")
                                       # Choices for the user.
        if choice == "1":
            book_ticket(username)

        elif choice == "2":
            view_my_tickets(username)

        elif choice == "3":
            search_ticket()

        elif choice == "4":
            cancel_ticket(username)

        elif choice == "5":
            print("\nLogging out.....")
            break

        else:
            print("\nInvalid choice. Please try again.")


#=========================================================
#                   USER DATA 
#=========================================================
                        
users = {                                     #User/Admin datas for the developers to login in to the program.
    "admin":{
        "password" : "admin123",
        "role" : "admin"
    },

    "student" : {
        "password" : "student123",
        "role" : "user"
    }
}


#========================================================
#                    TICKET DATA
#======================================================= 
                      
tickets = []
next_pnr = 100001


#========================================================
#                    LOGIN SYSTEM
#========================================================
                                               # Program starts from here, login details to be given
def login():
    print("\n=========================================")
    print("          RAILWAY TICKETING SYSTEM         ")
    print("===========================================")

    username = input("Enter username:")        #Username - student (for users) , Username - admin(for admin)
    password = input("Enter password:")        #Password - student123           , Password - admin123

    if username in users:
        if users[username]["password"] == password:
            print("\nLogin successful!")
            print("Welcome,",username)

            return username

        else:
            print("\nIncorrect password.")
    else:
        print("\nUsername not found.")

    return None

#========================================================
#                    BOOK TICKET
#========================================================

def book_ticket(username):             # Here the user enters the data for booking a ticket.

    global next_pnr

    print("\n=========================================")
    print("             BOOK TICKET                   ")
    print("===========================================")

    print("\nAvailable Trains")
    print("-----------------------------------------")
    print("1. 12001 - Bhopal Shatabdi")
    print("2. 12101 - Jnaneswari Express")
    print("3. 12622 - Tamil Nadu Express")
    print("4. 12951 - Mumbai Rajdhani")

    train_choice = input("\nChoose train:")

    if train_choice == "1":
        train_number = "12001"
        train_name = "Bhopal Shatabdi"

    elif train_choice == "2":
        train_number = "12101"
        train_name = "Jnaneswari Express"

    elif train_choice == "3":
        train_number = "12622"
        train_name = "Tamil Nadu Express"

    elif train_choice == "4":
        train_number = "12951"
        train_name = ("Mumbai Rajdhani")

    else:
        print("\nInvalid train selection.")
        return

    origin = input("\nEnter origin station:")
    destination = input("Enter destination station:")

    if origin.lower() == destination.lower():

        print("\nOrigin and destination cannot be the same.")
        return

    travel_date = input("Enter travel date (DD-MM-YYYY) :")

    try:
        passengers = int(input("Enter the number of passengers :"))

        if passengers <= 0 :
            print("Number of passengers must be greater than zero.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    passenger_name = []

    print("\nEnter passenger names:")

    for i in range(passengers):
        name = input("Passenger" + str(i + 1) + ": ")
        passenger_name.append(name)

    ticket = {
        "pnr" : next_pnr,
        "username" : username,
        "train_number" : train_number,
        "train_name" : train_name,
        "origin" : origin,
        "destination" : destination,
        "travel_date" : travel_date,
        "passengers" : passenger_name,
        "status" : "Confirmed"
    }

    tickets.append(ticket)
    print("\n===================================")
    print("         TICKET BOOKED SUCCESSFULLY")
    print("=====================================")

    print("PNR Number :", next_pnr)
    print("Train      :", train_number, "-", train_name)
    print("Origin     :",origin)
    print("Destination:",destination)
    print("Travel date:",travel_date)
    print("Passengers :",passengers)
    print("Status     : Confirmed")

    print("======================================")

    next_pnr += 1


# ====================================================
#                VIEW USER TICKETS 
#=====================================================

def view_my_tickets(username):
    print("\n=================================")
    print("              MY BOOKINGS")
    print("===================================")

    found = False

    for ticket in tickets:
        if ticket["username"] == username:
            found = True

            print("\nPNR Number:" , ticket["pnr"])
            print("Train       :", ticket["train_number"],
                  "-",ticket["train_name"])
            print("From        :", ticket["origin"])
            print("To          :",ticket["destination"])
            print("Date        :",ticket["travel_date"])

            print("Passengers:")

            for passenger in ticket["passengers"]:
                print(" -", passenger)

            print("Status   :", ticket["status"])

            print("-------------------------------------")

        if found == False:
            print("You have no bookings.")

#======================================================
#                 SEARCH TICKET
#======================================================

def search_ticket():
    print("\n===================================")
    print("                SEARCH TICKET")
    print("=====================================")

    try:
        pnr = int(input("Enter PNR Number:"))
    except ValueError:
        print("Please enter a valid PNR number.")
        return
    
    for ticket in tickets:
        if ticket["pnr"] == pnr:
            print("\nTicket Found!")
            print("--------------------------")

            print("PNR Number:", ticket["pnr"])
            print("User      :", ticket["username"])
            print("Train     :", ticket["train_number"],
                  "-", ticket["train_name"])
            print("From      :", ticket["origin"])
            print("To        :", ticket["destination"])
            print("Date      :", ticket["travel_date"])

            print("Passengers:")

            for passenger in ticket["passengers"]:
                print("  -", passenger)

            print("Status  :", ticket["status"])

            print("----------------------------")
            return
    print("\nPNR number not found.")

#=================================================
#                 CANCEL TICKET
#=================================================

def cancel_ticket(username): 
    print("\n=================================")
    print("               CANCEL TICKET")
    print("===================================")

    try:
        pnr = int(input("Enter PNR Number:"))

    except ValueError:
        print("Invalid PNR number.")
        return

    for ticket in tickets:
        if ticket["pnr"] == pnr:
            if ticket["username"] != username:

                print("\nYou can cancel only your own tickets.")
                return

            if ticket["status"] == "Cancelled":
                print("\nThis ticket is already cancelled.")
                return

            ticket["status"] = "Cancelled"
            print("\nTicket cancelled successfully.")
            print("PNR Number:",pnr)
            return

    print("\nTicket not found.")

#===================================================
# 9. ADMIN MENU
#===================================================

def admin_menu(username):

    while True:
        print("\n====================================")
        print("         ADMIN MENU")
        print("======================================")

        print("Logged in as:",username)

        print("\n1.View All Bookings")
        print("2. Search Ticket")
        print("3. Cancel Booking")
        print("4. Railway Statsitics")
        print("6. Logout")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            view_all_tickets()

        elif choice == "2":
            search_ticket()

        elif choice == "3":
            admin_cancel_ticket()

        elif choice == "4":
            railway_statistics()

        elif choice == "5":
            print("\nLogging Out......")
            break

        else:
            print("\nInvalid choice. Please try again")

#===============================================
# 10. VIEW ALL TICKETS
#===============================================

def view_all_tickets():
    print("\n===================================")
    print("              ALL BOOKINGS")
    print("=====================================")

    if len(tickets) == 0:
        print("No bookings available.")
        return

    for ticket in tickets:
        print("\nPNR Number:", ticket["pnr"])

        print("User  :", ticket["username"])

        print("Train     :", ticket["train_number"], ticket["train_name"])

        print("To     :", ticket["destination"])

        print("Travel Date: ", ticket["travel_date"])
        print("Passengers:")

        for passenger in ticket["passengers"]:
            print("  -",passenger)

        print("Status  :",ticket["status"])

        print("--------------------------------------")

#====================================================
# 11. ADMIN CANCEL TICKET
#====================================================

def admin_cancel_ticket():
    print("\n=================================")
    print("           CANCEL BOOKING")
    print("===================================")

    try:
        pnr = int(input("Enter PNR Number:"))

    except ValueError:
        print("Invalid PNR number:")

    for ticket in tickets:
        if ticket["pnr"] == pnr:
            if ticket["status"] == "Cancelled":
                print("\nTicket is already cancelled")
                return
            ticket["status"] == "Cancelled"
            print("\nTicket cancelled successfully.")
            return

    print("\nTicket not found.")

#===================================================
# 12. RAILWAY STATISTICS
#===================================================

def railway_statistics():
    print("\n======================================")
    print("       RAILWAY STATISTICS")
    print("========================================")

    totalbooking = len(tickets)
    confirmed = 0
    cancelled = 0
    totalpassengers = 0

    for ticket in tickets:
        if ticket["status"] == "Confirmed":
            confirmed += 1

        elif ticket["status"] == "Cancelled":
            cancelled += 1

        totalpassengers += len(ticket['passengers'])

    print("\nTotal Booking    :", totalbooking)
    print("Confirmed Bookings  :", confirmed)
    print("Cancelled Bookings  :", cancelled)
    print("Total Passengers  :" , totalpassengers)

#====================================================
#   13. MAIN PROGRAM
#====================================================

while True:
    print("\n===================================")
    print("   RAILWAY TICKETING SYSTEM")
    print("=====================================")

    print("\n1. User Login")
    print("2. Admin Login")
    print("3. Exit")

    choice = input("\nEnter your choice:")

    # ---------------- USER LOGIN ----------------

    if choice == "1":
        username = login()

        if username is not None:
            if users[username]["role"] == "user":
                user_menu(username)

            else:
               print("\nPlease use the Admin Login option")

    #----------------- ADMIN LOGIN ---------------

    elif choice == "2":
        username = login()

        if username is not None:
            if users[username]["role"] == "admin":
                admin_menu(username)
            else:
                print("\nYou do not have admin access.")


    #----------------- EXIT -------------------------
     
    elif choice == "3":
        print("\nThank you for using the")
        print("Railay Ticketing System!")

        break

    else: 
        print("\nInvalid Choice. Please try again.")

