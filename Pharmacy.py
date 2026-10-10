import sqlite3
import re

############## PASSWORD VALIDATION ###################

def validate_password(password):
    validate=r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*])(?=.*\d)[A-Za-z\d!@#$%^&*]{8,}$"

    if re.match(validate,password):
        return True
    else:
        return False

############### SIGN UP ################################


def sign_up():

    con = sqlite3.connect("pharmacy.db")
    c = con.cursor()

    print("\n=============== SIGN UP ===============")

    user_name = input("Enter username: ")

    # Check if username already exists
    c.execute("SELECT user_name FROM USERS WHERE user_name=?", (user_name,))

    if c.fetchone():
        print("Username already exists. Please choose a different username.")

    else:

        password = input("Enter password: ")

        if validate_password(password):

            role = input("Enter role (user/pharmacist): ")

            c.execute(
                "INSERT INTO USERS(user_name, password, role) VALUES(?,?,?)",
                (user_name, password, role)
            )

            con.commit()

            print("User registered successfully.")

            # --------------------------------
            # PHARMACIST DETAILS
            # --------------------------------

            if role.lower() == "pharmacist":

                print("\n=============== PHARMACIST DETAILS ===============")

                pharmacist_id = input("Enter pharmacist ID: ")
                pharmacist_name = input("Enter pharmacist name: ")
                phone = input("Enter phone number: ")
                email = input("Enter email: ")
                license_number = input("Enter license number: ")
                joining_date = input("Enter joining date: ")

                c.execute(
                    """
                    INSERT INTO PHARMACISTS
                    (user_name, pharmacist_id, pharmacist_name,
                     phone_number, email, license_number, joining_date)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        user_name,
                        pharmacist_id,
                        pharmacist_name,
                        phone,
                        email,
                        license_number,
                        joining_date
                    )
                )

                con.commit()

                print("Pharmacist details added successfully.")

        else:
            print("Password does not meet the requirements. Please try again.")

    con.close()


################## LOGIN #########################
def login():
    con=sqlite3.connect("pharmacy.db")
    c=con.cursor()

    print("\n =============== LOGIN ===============")
    user_name=input("Enter username:")
    password=input("Enter password:")
    role=input("Enter role(user/pharmacist):")

    c.execute("SELECT user_name,password,role FROM USERS WHERE user_name=? AND password=? AND role=?",
    (user_name,password,role))
    user = c.fetchone()
    if user is None:
        print("Invalid username, password, or role. Please try again.")
        con.close()
        return
        print("\nLogin successful!")
        print("Welcome,", user[1])
        print("Role:", user[2])
        con.close()

################### ROLE BASED MENU #########################
    if user[2] == "user":
        user_menu(user[0])
    elif user[2] == "pharmacist":
        pharmacist_menu()

################## USER MENU #########################
def user_menu(username):
    while True:
        print("\n =============== USER MENU ===============")
        print("1. View Medicines")
        print("2.View Bills")
        print("3. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_medicines()
        elif choice == "2":
            view_bills(username)
        elif choice == "3":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

#################  PHARMACIST MENU #########################
def pharmacist_menu():
    while True:
        print("\n =============== PHARMACIST MENU ===============")
        print("1. Add Medicine")
        print("2. View Medicines")
        print("3. Update Medicine")
        print("4. Delete Medicine")
        print("5. Generate Bill")
        print("6. Logout")

        choice = input("Enter your choice : ")

        if choice == "1":
            add_medicines()
        elif choice == "2":
            view_medicines()
        elif choice == "3":
            update_medicines()
        elif choice == "4":
            delete_medicines()
        elif choice == "5":
            generate_bill()
        elif choice == "6":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

#################### ADD MEDICINES #########################

def add_medicines():
    con=sqlite3.connect("pharmacy.db")
    c=con.cursor()

    print("\n =============== ADD MEDICINE ===============")
    medicine_id=input("Enter medicine ID:")
    medicine_name=input("Enter medicine name:")
    manufacturer=input("Enter manufacturer:")
    price=float(input("Enter price:"))
    quantity=int(input("Enter quantity:"))
    expiry_date=input("Enter expiry date (YYYY-MM-DD):")

    c.execute('INSERT INTO MEDICINES(medicine_id,medicine_name,manufacturer,price,quantity,expiry_date) VALUES(?,?,?,?,?,?);',(medicine_id,medicine_name,manufacturer,price,quantity,expiry_date))

    con.commit()
    print("Medicine added successfully.")

    con.close()

########################## VIEW MEDICINES #########################
def view_medicines():
    con=sqlite3.connect("pharmacy.db")
    c=con.cursor()

    print("\n =============== VIEW MEDICINES ===============")
    c.execute('''
    SELECT medicine_id, medicine_name, manufacturer, price, quantity, expiry_date
    FROM MEDICINES
    ''')
    medicines = c.fetchall()
    
    if medicines is None:
        print("No medicines found.")
    else:
        for medicine in medicines:
            print("\nMedicine ID:", medicine[0])
            print("Medicine Name:", medicine[1])
            print("Manufacturer:", medicine[2])
            print("Price:", medicine[3])
            print("Quantity:", medicine[4])
            print("Expiry Date:", medicine[5])
            print("\n-----------------------------")
    
    con.close()

################## VIEW BILLS ##############################

def view_bills(username):

    con = sqlite3.connect("pharmacy.db")
    c = con.cursor()

    print("\n=============== MY BILLS ===============")

    c.execute("""
        SELECT
            bill_id,
            pharmacist_id,
            number_of_items,
            amount,
            total_price,
            bill_date
        FROM BILL
        WHERE user_name = ?
    """, (username,))

    bills = c.fetchall()

    if not bills:
        print("\nNo bills found.")

    else:

        print("\n========== BILL DETAILS ==========")

        for bill in bills:

            print("\nBill ID:", bill[0])
            print("Pharmacist ID:", bill[1])
            print("Number of Items:", bill[2])
            print("Amount:", bill[3])
            print("Total Price:", bill[4])
            print("Bill Date:", bill[5])

            print("--------------------------------")

    con.close()

################## UPDATE MEDICINES ##########################

def update_medicines():
    con=sqlite3.connect("pharmacy.db")
    c=con.cursor()

    print("\n =============== UPDATE MEDICINE ===============")
    medicine_id = input("Enter medicine ID to update: ")
    c.execute('SELECT * FROM MEDICINES WHERE medicine_id = ?', (medicine_id,))
    medicine = c.fetchone()
    if medicine is None:
        print("Medicine not found.")
    else:
        print("Current details:")
        print("Medicine ID:", medicine[0])
        print("Medicine Name:", medicine[1])
        print("Manufacturer:", medicine[2])
        print("Price:", medicine[3])
        print("Quantity:", medicine[4])
        print("Expiry Date:", medicine[5])

        print("\n Enter new details (press Enter to keep current value):")
        medicine_name = input("Enter new medicine name: ") or medicine[1]
        manufacturer = input("Enter new manufacturer: ") or medicine[2]
        price = float(input("Enter new price: ") or medicine[3])
        quantity = int(input("Enter new quantity: ") or medicine[4])
        expiry_date = input("Enter new expiry date (YYYY-MM-DD): ") or medicine[5]

        c.execute('''
            UPDATE MEDICINES
            SET medicine_name = ?, manufacturer = ?, price = ?, quantity = ?, expiry_date = ?
            WHERE medicine_id = ?
        ''', (medicine_name, manufacturer, price, quantity, expiry_date, medicine_id))

        con.commit()
        print("Medicine updated successfully.")

    con.close()

####################### DELETE MEDICINES ##########################

def delete_medicines():
    con=sqlite3.connect("pharmacy.db")
    c=con.cursor()

    print("\n =============== DELETE MEDICINE ===============")
    medicine_id = input("Enter medicine ID to delete: ")
    c.execute('SELECT * FROM MEDICINES WHERE medicine_id = ?', (medicine_id,))
    medicine = c.fetchone()
    if medicine is None:
        print("Medicine not found.")
    else:
        c.execute('DELETE FROM MEDICINES WHERE medicine_id = ?', (medicine_id,))
        con.commit()
        print("Medicine deleted successfully.")

    con.close()

###################### GENERATE BILL ##########################
def generate_bill():

    con = sqlite3.connect("pharmacy.db")
    c = con.cursor()

    print("\n =============== GENERATE BILL ===============")
    pharmacist_id = input("Enter pharmacist ID: ")
    user_name=input("Enter customer username: ")

    c.execute(
    "SELECT user_name FROM USERS WHERE user_name=? AND role='user'",
    (user_name,)
    )
    customer = c.fetchone()

    if customer is None:
        print("Customer not found.")
        con.close()
        return

    number_of_items = int(input("Enter number of medicines: "))
    total_price = 0

    print("\n--------------- BILL ----------------")

    for i in range(number_of_items):

        medicine_id = input("Enter medicine ID: ")

        c.execute(
            "SELECT medicine_name, price, quantity FROM MEDICINES WHERE medicine_id=?",
            (medicine_id,)
        )

        medicine = c.fetchone()

        if medicine is None:
            print("Medicine not found.")
            continue

        medicine_name = medicine[0]
        price = medicine[1]
        available_quantity = medicine[2]

        quantity = int(input("Enter quantity: "))

        if quantity > available_quantity:
            print("Not enough stock available.")
            continue

        amount = price * quantity
        total_price = total_price + amount

        print("\nMedicine:", medicine_name)
        print("Price:", price)
        print("Quantity:", quantity)
        print("Amount:", amount)

        # Reduce medicine quantity
        new_quantity = available_quantity - quantity

        c.execute(
            "UPDATE MEDICINES SET quantity=? WHERE medicine_id=?",
            (new_quantity, medicine_id)
        )

    bill_date = input("Enter bill date (YYYY-MM-DD): ")

    c.execute(
        '''INSERT INTO BILL
        (user_name,pharmacist_id, amount, number_of_items, total_price, bill_date)
        VALUES (?,?, ?, ?, ?, ?)''',
        (user_name,pharmacist_id, total_price, number_of_items, total_price, bill_date)
    )

    con.commit()

    print("\n====================================")
    print("          BILL GENERATED")
    print("====================================")
    print("Pharmacist ID:", pharmacist_id)
    print("Customer username:", user_name)
    print("Number of Items:", number_of_items)
    print("Name of Medicines:", [medicine_name for i in range(number_of_items)])
    print("Total Amount:", total_price)
    print("Bill Date:", bill_date)
    print("====================================")

    con.close()

##################### MAIN MENU ##############################
while True:
    print("\n =============== PHARMACY MANAGEMENT SYSTEM ===============")
    print("1. Sign Up")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice : ")

    if choice == "1":
        sign_up()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")


