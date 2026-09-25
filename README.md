# Railway Ticketing  Management System

## Project Overview

The Railway Ticketing System is a Python-based console application designed to manage basic railway ticket booking operations.

The system provides separate access for users and administrators. Users can book tickets, view their bookings, search for tickets, and cancel their own tickets. Administrators can view all bookings, search and cancel bookings, and view railway statistics.

The project uses a menu-driven approach to provide a simple and organized way to interact with the railway ticketing system.

---

## Objectives
- To create a simple railway ticket booking system.
- To provide separate User and admin access.
- To collect and manage passengers and journey information.
- To generate unique PNR numbers for bookings.
- To allow users to view and cancel their bookings.
- To provide ticket searching using PNR numbers.
- To allow administrators to monitor all bookings.
- To calculate basic railway booking statistics.
- To demonstrate practical python programming concepts.

---

## Features

- User and administrator login
- Railway ticket booking
- Train selection
- Passenger details management
- Automatic PNR generation
- View and search bookings
- Ticket cancellation
- Booking status management
- Railway booking statistics
- Input validation and error handling
- Menu-driven console interface

--- 

## Technologies/Tools Used

* Python 3
* Python functions
* Conditional statements
* Loops
* Lists
* Dictionaries
* Input validation
* Console/Terminal
* Git and GitHub for version control

The current project does not require any external Python libraries.

---

## Installation and Setup

Follow the steps below to install and run the project on your computer.

Step 1: Install Python

Download and install Python 3 on your computer.

After installation, open Command Prompt / Terminal and check whether Python is installed:

python --version

If that command does not work, try:

python3 --version

You should see the installed Python version.
---
Step 2: Download the Project

You can either clone the GitHub repository or download it as a ZIP file.

Option 1 — Clone using Git

Open Command Prompt or Terminal and run:

git clone <your-github-repository-url>

Then move into the project folder:

cd Railway-Ticketing-Management-System\
Option 2 — Download ZIP\
Open the GitHub repository.\
Click Code.\
Select Download ZIP.\
Extract the ZIP file.\
Open the extracted project folder.
---
Step 3: Check the Project Files

Make sure the project folder contains:

- project1.py
- README.md
- statement.md
---
Step 4: Run the Program

Open Command Prompt or Terminal inside the project folder.

Run:

python project1.py

If your system uses python3, run:

python3 project1.py

---

## Login Details

The current version uses predefined login credentials.

### User
* Username: student
* Password: student123
### Admin
* Username: admin
* Passwgord: admin123

Note: These credentials are included directly in the source code for this project.

---

## Instructions for Testing

Test 1: User Login

Start the program.

Select 1. User Login.

Enter:

Username: student

Password: student123

Confirm that the User Menu is displayed.

---

Test 2: Book a Ticket

Log in as a user.

Select Book Railway Ticket.

Select one of the available trains.

Enter an origin station.

Enter a different destination station.

Enter a travel date.

Enter the number of passengers.

Enter the passenger names.

Confirm that a PNR number is generated and the booking status is shown as Confirmed.

---


Test 3: View Bookings

From the User Menu, select View My Bookings.

Verify that the newly created booking is displayed.

Check the PNR, train, origin, destination, travel date, passengers, and status.

Test 4: Search Ticket

Select Search Ticket.

Enter the PNR number of an existing booking.

Verify that the ticket details are displayed.

Test an invalid PNR to verify that the system reports that the ticket was not found.

---


Test 5: Cancel Ticket

Select Cancel Ticket.

Enter the PNR of the user's booking.

Verify that the ticket status changes to Cancelled.

Try cancelling the same ticket again and verify that the system identifies it as already cancelled.

---


Test 6: Admin Login

Return to the main menu.

Select Admin Login.

Enter:

Username: admin

Password: admin123

Confirm that the Administrator Menu is displayed.

---


Test 7: View All Bookings

Select View All Bookings.

Verify that the bookings created during testing are displayed.

Check that the booking information is shown correctly.

---


Test 8: Railway Statistics

From the Administrator Menu, select Railway Statistics.

Verify the displayed:

Total bookings

Confirmed bookings

Cancelled bookings

Total passengers

---


Test 9: Invalid Input Testing

Test the program with:

Incorrect username.

Incorrect password.

Invalid menu choice.

Invalid train selection.

Same origin and destination.

Zero or negative passenger count.

Non-numeric PNR.

Non-existent PNR.

Verify that the program displays an appropriate error message and continues to operate.

---

# Project File

Railway-Ticketing-System/
|
|-- project1.py\
|-- README.md  \
|-- statement.md

## Author 
Aditya Kumar Pandey
Project = Railway Ticketing Management System
Language : Python