# Pharmacy-Management-System

# Pharmacy Management System

## 1. Project Overview

The Pharmacy Management System is a command-line application developed using Python and SQLite. It helps manage pharmacy operations, including user registration, login, medicine inventory management, bill generation, and customer billing history.

The system provides two roles: **Pharmacist** and **User**. Pharmacists can manage medicine records and generate bills, while users can view available medicines and their bills.

## 2. Technologies Used

- **Python:** For application logic and user interaction.
- **SQLite:** For storing user accounts, pharmacist details, medicine inventory, and billing records.
- **DB Browser for SQLite:** For viewing and managing the database.
- **Regular Expressions (Regex):** For password validation.

## 3. Features

### User Authentication
- User and pharmacist registration.
- Login using username, password, and role.
- Password validation using regular expressions.

### Pharmacist Functions
- Add new medicines.
- View available medicines.
- Update medicine details.
- Delete medicine records.
- Generate bills for registered customers.
- Update medicine stock after billing.

### User Functions
- View available medicines.
- View personal billing history.
- Log out of the system.

## 4. Project Structure

The project folder contains the following files:

```text
Pharmacy_Management_System/
│
├── Pharmacy.py
├── pharmacy.db
└── README.md
```

- `Pharmacy.py` — Main Python program containing the application functions.
- `pharmacy.db` — SQLite database containing the project data. It may be created automatically when the program connects to it and creates the required tables.
- `README.md` — Documentation explaining the project and how to run it.

*Note: The filenames above are examples. Use your actual Python filename and database filename if they are different.*

## 5. Requirements

Before running the project, install or ensure the following are available:

- Python 3.x
- Visual Studio Code (VS Code)
- Python extension for VS Code
- DB Browser for SQLite (optional, for viewing database contents)

SQLite support is included in Python through the built-in `sqlite3` module. Therefore, installing a separate SQLite Python package is not required.

## 6. How to Run the Project

### Step 1: Install Python

Download and install Python from:

https://www.python.org/downloads/

During installation on Windows, enable the option **Add Python to PATH**.

### Step 2: Open the Project

1. Open Visual Studio Code.
2. Select **File → Open Folder**.
3. Select the folder containing your project files.

### Step 3: Check the Python File

Ensure that the main Python file, such as `Pharmacy.py`, contains the application code and that the database connection uses the intended database filename.

For example:

```python
import sqlite3

con = sqlite3.connect("pharmacy.db")
```

Make sure the required database tables are created before the application attempts to use them.

### Step 4: Open the Terminal

In VS Code, select **Terminal → New Terminal**.

Navigate to the project directory if the terminal is not already there.

### Step 5: Run the Program

Execute the following command, replacing the filename if necessary:

```bash
python Pharmacy.py
```

On some Windows installations, you may need to use:

```bash
py Pharmacy.py
```

### Step 6: Use the Application

The main menu appears:

```text
=============== PHARMACY MANAGEMENT SYSTEM ===============
1. Sign Up
2. Login
3. Exit
Enter your choice:
```

- Select **1 — Sign Up** to create a new account.
- Select **2 — Login** to log in with an existing account.
- Select **3 — Exit** to close the application.

### Step 7: Register and Log In

Create an account by entering a username, password, and role.

If registering as a pharmacist, provide the additional pharmacist details requested by the program.

After registration, return to the main menu and log in using the registered credentials and the correct role.

### Step 8: Access the Menus

**Pharmacist menu:**
1. Add Medicine
2. View Medicines
3. Update Medicine
4. Delete Medicine
5. Generate Bill
6. Logout

**User menu:**
1. View Medicines
2. View Bills
3. Logout

Follow the displayed prompts to perform the required operations.

## 7. Database Information

The project uses SQLite to store and retrieve information. The database includes tables for the following purposes, subject to the actual table definitions in the source code:

- **USERS:** Stores usernames, passwords, and user roles.
- **PHARMACISTS:** Stores pharmacist identification and professional details.
- **MEDICINES:** Stores medicine names, manufacturers, prices, quantities, and expiry dates.
- **BILLS / BILLING:** Stores billing information and transaction details.

The exact table names and columns should match those defined in the Python program.

## 8. Viewing the Database

To inspect the stored records:

1. Open DB Browser for SQLite.
2. Select **Open Database**.
3. Choose `pharmacy.db` from your project folder.
4. Open the **Browse Data** tab.
5. Select a table from the dropdown to view its records.

If the database file does not exist yet, run the Python program first so that the database and tables can be initialized.

## 9. Important Notes

- Run the application from the project folder so that the relative database path points to the intended file.
- Keep the database file and Python program in the appropriate locations.
- Register a customer account before generating a bill for that customer.
- Enter valid medicine IDs and quantities when generating bills.
- Ensure that sufficient stock is available before completing a transaction.
- Use a consistent date format when entering medicine expiry dates and bill dates.
- For demonstration purposes, use sample data rather than real customer information.

## 10. Conclusion

The Pharmacy Management System demonstrates how Python and SQLite can be combined to develop a basic database-driven application. It supports role-based access, medicine inventory operations, billing, and retrieval of customer billing records through a simple command-line interface.
