import sqlite3

# ---------------- DATABASE SETUP ----------------
conn = sqlite3.connect("expense_tracker.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT,
    category TEXT,
    amount REAL,
    date TEXT
)
""")

conn.commit()

# ---------------- FUNCTIONS ----------------

def add_income():
    amount = float(input("Enter income amount: "))
    date = input("Enter date (YYYY-MM-DD): ")

    cur.execute("INSERT INTO expenses (type, category, amount, date) VALUES (?, ?, ?, ?)",
                ("Income", "Salary", amount, date))
    conn.commit()
    print("Income added successfully!\n")


def add_expense():
    category = input("Enter category (Food/Travel/Bills/etc): ")
    amount = float(input("Enter expense amount: "))
    date = input("Enter date (YYYY-MM-DD): ")

    cur.execute("INSERT INTO expenses (type, category, amount, date) VALUES (?, ?, ?, ?)",
                ("Expense", category, amount, date))
    conn.commit()
    print("Expense added successfully!\n")


def view_data():
    print("\n------ ALL TRANSACTIONS ------")
    cur.execute("SELECT * FROM expenses")
    data = cur.fetchall()

    for row in data:
        print(row)
    print()


def show_summary():
    cur.execute("SELECT SUM(amount) FROM expenses WHERE type='Income'")
    income = cur.fetchone()[0] or 0

    cur.execute("SELECT SUM(amount) FROM expenses WHERE type='Expense'")
    expense = cur.fetchone()[0] or 0

    balance = income - expense

    print("\n------ SUMMARY ------")
    print("Total Income :", income)
    print("Total Expense:", expense)
    print("Balance      :", balance)
    print()


def delete_record():
    view_data()
    id = input("Enter ID to delete: ")

    cur.execute("DELETE FROM expenses WHERE id=?", (id,))
    conn.commit()
    print("Record deleted!\n")


# ---------------- MAIN MENU ----------------

while True:
    print("===================================")
    print("      SMART EXPENSE TRACKER")
    print("===================================")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View All Data")
    print("4. Show Summary")
    print("5. Delete Record")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_income()
    elif choice == "2":
        add_expense()
    elif choice == "3":
        view_data()
    elif choice == "4":
        show_summary()
    elif choice == "5":
        delete_record()
    elif choice == "6":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice!\n")

conn.close()
