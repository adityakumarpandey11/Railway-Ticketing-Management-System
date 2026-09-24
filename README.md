# Railway Ticketing Management System

## 📌 Project Overview

The **Railway Ticketing Management System** is a Python-based console application designed to manage basic railway ticketing operations.

The system provides separate access for **Users** and **Administrators**. Users can book railway tickets, view their bookings, search for tickets using a PNR number, and cancel their tickets. Administrators can view all bookings, search and cancel bookings, and view basic railway statistics.

---

## 🎯 Objectives

* To create a simple railway ticket booking system.
* To provide separate User and Admin access.
* To collect and manage passenger and journey information.
* To generate unique PNR numbers for bookings.
* To allow users to view and cancel their bookings.
* To provide ticket searching using PNR numbers.
* To allow administrators to monitor all bookings.
* To calculate basic railway booking statistics.
* To demonstrate practical Python programming concepts.

---

## ✨ Features

### 👤 User Features

* User login
* Book railway tickets
* Select available trains
* Enter origin and destination
* Enter travel date
* Book tickets for multiple passengers
* Automatic PNR generation
* View personal bookings
* Search tickets
* Cancel own tickets
* Logout

### 🛠️ Admin Features

* Admin login
* View all bookings
* Search tickets using PNR
* Cancel bookings
* View railway statistics
* Monitor confirmed and cancelled bookings
* Logout

---

## 🚆 Available Trains

| Train Number | Train Name         |
| ------------ | ------------------ |
| 12001        | Bhopal Shatabdi    |
| 12101        | Jnaneswari Express |
| 12622        | Tamil Nadu Express |
| 12951        | Mumbai Rajdhani    |

---

## 🔑 Login Details

The current version uses predefined login credentials.

### User

```text
Username: student
Password: student123
```

### Admin

```text
Username: admin
Password: admin123
```

> **Note:** These credentials are included directly in the source code for this project.

---

## 🧩 Project Modules

### 1. Login System

Authenticates the user and identifies whether the account belongs to a User or Administrator.

### 2. User Menu

Provides access to:

* Book Railway Ticket
* View My Bookings
* Search Ticket
* Cancel Ticket
* Logout

### 3. Ticket Booking

Collects:

* Train details
* Origin station
* Destination station
* Travel date
* Number of passengers
* Passenger names

A unique PNR number is generated for every booking.

### 4. Ticket Search

Allows users and administrators to search for a ticket using its PNR number.

### 5. Ticket Cancellation

Users can cancel their own tickets, while administrators can cancel bookings through the Admin Menu.

### 6. Railway Statistics

Displays:

* Total bookings
* Confirmed bookings
* Cancelled bookings
* Total passengers

---

## 🛠️ Technologies Used

* **Python 3**
* Lists
* Dictionaries
* Functions
* Loops
* Conditional Statements
* Exception Handling
* Console-based User Interface
* Git & GitHub

No external Python libraries are required for the current version.

---

## 📂 Project Structure

```text
Railway-Ticketing-Management-System/
│
├── project1.py
├── README.md
└── statement.md
```

---

# ⚙️ Installation and Setup

Follow the steps below to install and run the project on your computer.

## Step 1: Install Python

Download and install **Python 3** on your computer.

After installation, open **Command Prompt / Terminal** and check whether Python is installed:

```bash
python --version
```

If that command does not work, try:

```bash
python3 --version
```

You should see the installed Python version.

---

## Step 2: Download the Project

You can either clone the GitHub repository or download it as a ZIP file.

### Option 1 — Clone using Git

Open Command Prompt or Terminal and run:

```bash
git clone <your-github-repository-url>
```

Then move into the project folder:

```bash
cd Railway-Ticketing-Management-System
```

### Option 2 — Download ZIP

1. Open the GitHub repository.
2. Click **Code**.
3. Select **Download ZIP**.
4. Extract the ZIP file.
5. Open the extracted project folder.

---

## Step 3: Check the Project Files

Make sure the project folder contains:

```text
project1.py
README.md
statement.md
```

---

## Step 4: Run the Program

Open Command Prompt or Terminal inside the project folder.

Run:

```bash
python project1.py
```

If your system uses `python3`, run:

```bash
python3 project1.py
```

---

## Step 5: Login

After running the program, the main menu will appear:

```text
===================================
   RAILWAY TICKETING SYSTEM
===================================

1. User Login
2. Admin Login
3. Exit
```

### To use the User section

Select:

```text
1
```

Then enter:

```text
Username: student
Password: student123
```

### To use the Admin section

Select:

```text
2
```

Then enter:

```text
Username: admin
Password: admin123
```

---

## Step 6: Book a Ticket

After logging in as a user:

1. Select **Book Railway Ticket**.
2. Select a train.
3. Enter the origin station.
4. Enter the destination station.
5. Enter the travel date.
6. Enter the number of passengers.
7. Enter passenger names.
8. The system generates a PNR number.
9. The booking is stored with a **Confirmed** status.

---

## Step 7: View or Search a Ticket

From the User Menu:

```text
1. Book Railway Ticket
2. View My Bookings
3. Search Ticket
4. Cancel Ticket
5. Logout
```

Select **View My Bookings** to display your bookings.

Select **Search Ticket** and enter the PNR number to find a particular ticket.

---

## Step 8: Cancel a Ticket

Select:

```text
4. Cancel Ticket
```

Enter the PNR number.

The system checks whether the ticket belongs to the logged-in user before cancelling it.

---

## Step 9: Use the Admin Panel

Login using:

```text
Username: admin
Password: admin123
```

The administrator can:

* View all bookings
* Search tickets
* Cancel bookings
* View railway statistics
* Logout

---

# 🔄 System Workflow

```text
                    START
                      |
                      v
          Railway Ticketing System
                      |
             -------------------
             |                 |
             v                 v
        User Login        Admin Login
             |                 |
             v                 v
         User Menu         Admin Menu
             |                 |
       ---------------    ---------------
       |      |      |    |      |      |
       v      v      v    v      v      v
      Book   View   Search View  Search Statistics
             |      |     All
             v      v
           Cancel  Ticket
             |
             v
            EXIT
```

---

## 💾 Data Management

The current version uses Python's built-in data structures to store information during program execution.

### User Data

User credentials and roles are stored in a dictionary.

### Ticket Data

Ticket information is stored in a list.

Each ticket contains:

```text
PNR
Username
Train Number
Train Name
Origin
Destination
Travel Date
Passengers
Status
```

---

## 🧪 Testing

| Test                        | Expected Result               |
| --------------------------- | ----------------------------- |
| Correct username/password   | Login successful              |
| Incorrect password          | Error message                 |
| Invalid train selection     | Selection rejected            |
| Same origin and destination | Booking rejected              |
| Invalid passenger count     | Error message                 |
| Valid PNR                   | Ticket displayed              |
| Invalid PNR                 | Ticket not found              |
| Valid cancellation          | Ticket cancelled              |
| Already cancelled ticket    | Cancellation rejected         |
| No existing bookings        | Appropriate message displayed |

---

## ⚠️ Current Limitations

* Booking data is stored temporarily in memory.
* Data is lost when the program is closed.
* No real railway database is connected.
* No online payment system.
* No real-time seat availability.
* No email or SMS notifications.
* No user registration system.
* Passwords are not encrypted.
* Train information is currently predefined.

---

## 🚀 Future Enhancements

1. **CSV or Database Storage**

   * Permanently store users and bookings.

2. **Train Management**

   * Allow administrators to add, remove, and modify trains.

3. **Seat Availability**

   * Track available and occupied seats.

4. **Fare Calculation**

   * Automatically calculate ticket prices.

5. **User Registration**

   * Allow passengers to create accounts.

6. **Secure Authentication**

   * Implement secure password storage.

7. **Database Integration**

   * Use SQLite or another database system.

8. **Graphical User Interface**

   * Convert the console application into a GUI.

9. **Digital Ticket Generation**

   * Generate a printable railway ticket.

10. **Advanced Train Search**

    * Search trains based on origin, destination, and travel date.

---

## 📚 Python Concepts Demonstrated

* Variables
* Data types
* Input and output
* `if`, `elif`, and `else`
* `for` loops
* `while` loops
* Lists
* Dictionaries
* Functions
* String manipulation
* Exception handling
* Data processing
* Modular programming
* Basic authentication
* Input validation

---

## 👨‍💻 Author

**Aditya Kumar Pandey**

**Project:** Railway Ticketing Management System

**Language:** Python
