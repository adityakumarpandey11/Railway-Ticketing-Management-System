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

Python 3

Python functions

Conditional statements

Loops

Lists

Dictionaries

Input validation

Console/Terminal

Git and GitHub for version control

The current project does not require any external Python libraries.

---

# Installation

Prerequisites

• Python 3 installed on your computer.
• Git installed if you want to clone the repository.
• A terminal or command prompt to run the project.
• No additional Python libraries are required.

Check whether Python is installed by running:

python --version

If your system uses python3, run:

python3 --version

Clone the Repository

Clone the project repository:

git clone <repository-url>

Open the project directory:

cd <project-folder>

No additional packages are required.

How to Run the Project

Run the Python program using:

python project1.py

Or, on systems that use python3:

python3 project1.py

The Railway Ticketing System main menu will appear after the program starts.

---

# Login Details

The current program contains sample login credentials.

User Login

Username: student
Password: student123

Admin Login

Username: admin
Password: admin123

These credentials are included in the source code for demonstration and testing.

---

# Instructions for Testing

Test 1: User Login

Start the program.

Select 1. User Login.

Enter:

Username: student

Password: student123

Confirm that the User Menu is displayed.

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

Test 3: View Bookings

From the User Menu, select View My Bookings.

Verify that the newly created booking is displayed.

Check the PNR, train, origin, destination, travel date, passengers, and status.

Test 4: Search Ticket

Select Search Ticket.

Enter the PNR number of an existing booking.

Verify that the ticket details are displayed.

Test an invalid PNR to verify that the system reports that the ticket was not found.

Test 5: Cancel Ticket

Select Cancel Ticket.

Enter the PNR of the user's booking.

Verify that the ticket status changes to Cancelled.

Try cancelling the same ticket again and verify that the system identifies it as already cancelled.

Test 6: Admin Login

Return to the main menu.

Select Admin Login.

Enter:

Username: admin

Password: admin123

Confirm that the Administrator Menu is displayed.

Test 7: View All Bookings

Select View All Bookings.

Verify that the bookings created during testing are displayed.

Check that the booking information is shown correctly.

Test 8: Railway Statistics

From the Administrator Menu, select Railway Statistics.

Verify the displayed:

Total bookings

Confirmed bookings

Cancelled bookings

Total passengers

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
|-- project1.py
|-- README.md   

---

## Author 
Aditya Kumar Pandey
Project = Railway Ticketing Management System
Language : Python