import sqlite3

con = sqlite3.connect("pharmacy.db")
c = con.cursor()

con.execute('''
CREATE TABLE USERS (
    user_name TEXT PRIMARY KEY NOT NULL,
    password TEXT NOT NULL,
    role TEXT NOT NULL
);
''')

con.execute('''
CREATE TABLE PHARMACISTS(
    user_name TEXT PRIMARY KEY NOT NULL,
    pharmacist_id INTEGER UNIQUE NOT NULL,
    pharmacist_name TEXT NOT NULL,
    phone_number TEXT NOT NULL,
    email TEXT NOT NULL,
    license_number TEXT NOT NULL,
    joining_date TEXT NOT NULL,
    FOREIGN KEY(user_name) REFERENCES USERS(user_name)
);
''')

con.execute('''
CREATE TABLE MEDICINES(
    medicine_id INTEGER PRIMARY KEY NOT NULL,
    medicine_name TEXT NOT NULL,
    manufacturer TEXT NOT NULL,
    price REAL NOT NULL,
    quantity INTEGER NOT NULL,
    expiry_date TEXT NOT NULL
);
''')

con.execute('''
CREATE TABLE BILL(
    bill_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_name TEXT NOT NULL,
    pharmacist_id INTEGER NOT NULL,
    amount REAL NOT NULL,
    number_of_items INTEGER NOT NULL,
    total_price REAL NOT NULL,
    bill_date TEXT NOT NULL,
    FOREIGN KEY(user_name) REFERENCES USERS(user_name),
    FOREIGN KEY(pharmacist_id) REFERENCES PHARMACISTS(pharmacist_id)
);
''')

con.commit()
con.close()

print("Database and tables created successfully.")