# Main Menu Functions
def main_menu():
    print_main_menu()
    while True:
        try:
            choice = int(input("Please select an option (1-7): "))
            if not validate_main_choice(choice):
                print("Please enter a valid number.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue
        break
    if choice == 1:
        item_menu()
    elif choice == 2:
        supplier_menu()
    elif choice == 3:
        hospital_menu()
    elif choice == 4:
        print_user_list()
        register()
    elif choice == 5:
        print_user_list()
        delete()
    elif choice == 6:
        restart_system()
        main_menu()
    elif choice == 7:
        exit()

def item_menu():
    print_item_menu()
    while True:
        try:
            choice = int(input("Please select an option (1-7): "))
            if not validate_item_choice(choice):
                print("Please enter a valid number.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue
        break
    if choice == 1:
        edit_item_stock()
    elif choice == 2:
        edit_item_supplier()
    elif choice == 3:
        print_item_list()
        item_menu()
    elif choice == 4:
        print_low_stock_item()
        item_menu()
    elif choice == 5:
        receive_item()
    elif choice == 6:
        distribute_item()
    elif choice == 7:
        main_menu()

def restart_system_menu():
    print_restart_system()
    while True:
        try:
            choice = int(input("Please select an option (1-2): "))
            if not validate_restart_system(choice):
                print("Please enter a valid number.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue
        break
    if choice == 1:
        restart_system()
        login()
    elif choice == 2:
        login()

def supplier_menu():
    # Placeholder for supplier menu function
    pass

def hospital_menu():
    # Placeholder for hospital menu function
    pass

# System Restart Function
def restart_system():
    users = [["admin", "admin"]]
    suppliers = [
        ["Supplier A", "A", "03-80421760", "22, Jalan TPP 2/2, Taman Perindustrian Puchong, 47100 Puchong, Selangor."],
        ["Supplier B", "B", "03-33443333", "30-2, Jalan Harmoni 1, Balakong, 43300 Seri Kembangan, Selangor."],
        ["Supplier C", "C", "03-89255099", "28 GF, Jalan 15/2, Seksyen 15, 43650 Bandar Baru Bangi, Selangor."],
        ["Supplier D", "D", "03-38953248", "No.20, Jalan Bayi Tinggi 3, KS6, Batu Unjur, 41200 Klang, Selangor."]
    ]
    hospitals = [
        ["Hospital A", "A", "03-26267777", "Jalan Raja, 50588 Kuala Lumpur, Wilayah Persekutuan Kuala Lumpur."],
        ["Hospital B", "B", "03-91563999", "2, Jalan 2/96b, Taman Cheras Indah, 56100 Kuala Lumpur, Wilayah Persekutuan Kuala Lumpur."],
        ["Hospital C", "C", "03-79557777", "Lot 70, 14 Jalan 14/7, Seksyen 14, 46300 Petaling Jaya, Selangor."],
        ["Hospital D", "D", "03-42996111", "2, Jalan Mamanda 10, Taman Dato Ahmad Said, 68000 Ampang, Selangor."]
    ]
    items = [
        ["Head cover", "HC", "A", "100 boxes"],
        ["Face shield", "FS", "B", "100 boxes"],
        ["Mask", "MS", "C", "100 boxes"],
        ["Gloves", "GL", "D", "100 boxes"],
        ["Gown", "GW", "A", "100 boxes"],
        ["Shoe covers", "SC", "B", "100 boxes"]
    ]
    write_user(users)
    write_supplier(suppliers)
    write_hospital(hospitals)
    write_item(items)
    open("distribution.txt", "w").close()
    open("receiving.txt", "w").close()

# User Management Functions
def login():
    num_attempts = 0
    while True:
        if not validate_num_attempt(num_attempts):
            exit()
        print_login_page()
        username = input("Enter Username to login: ").strip()
        password = input("Enter Password to login: ").strip()
        if validate_cred_user(latest_user(), username, password):
            print("Login Successful!\n")
            main_menu()
        else:
            print("Invalid username or password.\n")
            num_attempts += 1

def register():
    if validate_num_user(latest_user()):
        print_register_page()
        username = input("Enter Username to register: ").strip()
        password = input("Enter Password to register: ").strip()
        if validate_username(username):
            users = add_user(latest_user(), username, password)
            write_user(users)
        else:
            print("Username is already taken!\n")
        main_menu()
    else:
        print("MAX USER REACHED\n")
        main_menu()

def delete():
    print_delete_page()
    username = input("Enter Username to delete user: ").strip()
    password = input("Enter Password to delete user: ").strip()
    if username != "admin":
        if validate_cred_user(latest_user(), username, password):
            users = delete_user(latest_user(), username, password)
            write_user(users)
            main_menu()
        else:
            print("USER NOT FOUND\n")
            main_menu()
    else:
        print("Admin can't be deleted!\n")
        main_menu


def add_user(users, username, password):
    user_info = [username, password]
    users.append(user_info)
    return users


def delete_user(users, username, password):
    for user_info in users:
        if username == user_info[0] and password == user_info[1]:
            users.remove(user_info)
    return users

# Item Management Functions
def edit_item_stock():
    print_item_list()
    item_code = input("Enter item code:").upper().strip()
    if validate_item_code(latest_items(), item_code):
        try:
            item_stock = int(input("Enter new item stock: "))
            if validate_item_stock(item_stock):
                items = change_items_stock(latest_items(), item_code, item_stock)
                write_item(items)
                print("Item stock updated successfully!")
                item_menu()
            else:
                print("Invalid item stock. Returning to main menu...\n")
                item_menu()
        except ValueError:
            print("Invalid item stock. Returning to main menu...\n")
            item_menu()
    else:
        print("Invalid item code. Returning to main menu...\n")
        item_menu()

def edit_item_supplier():
    print_item_list()
    item_code = input("Enter item code: ").upper().strip()
    if validate_item_code(latest_items(), item_code):
        supplier_code = input("Enter new supplier code: ").upper().strip()
        if validate_item_supplier_code(latest_suppliers(), supplier_code):
            items = change_items_supplier(latest_items(), item_code, supplier_code)
            write_item(items)
            print("Item's supplier code updated successfully!\n")
            item_menu()
        else:
            print("Invalid supplier code. Returning to main menu...\n")
            item_menu()
    else:
        print("Invalid item code. Returning to main menu...\n")
        item_menu()

def print_item_list():
    items = latest_items()
    sorted_items = sorted(items, key=lambda x: x[1])
    print("Available items:")
    for i, item in enumerate(sorted_items):
        print(f"{i+1}. Item: {item[0]}, Item code: {item[1]}, Supplier code: {item[2]}, Stock: {item[3]}")
    print()

def print_low_stock_item():
    items = latest_items()
    j = 0
    for item_info in items:
        stock = int(item_info[3].split(" ")[0].strip())
        if stock < 25:
            j += 1
    if j >= 1:
        sorted_items = sorted(items, key=lambda x: x[3])
        print("Low stock item:")
        i = 1
        for item in sorted_items:
            stock = int(item[3].split(" ")[0])
            if stock < 25:
                print(f"{i}. Item: {item[0]}, Item code: {item[1]}, Supplier code: {item[2]}, Stock: {item[3]}")
                i += 1
    elif j < 1:
        print("No Low Stock Item")
    print()

def print_supplier_list():
    suppliers = latest_suppliers()
    sorted_suppliers = sorted(suppliers, key=lambda x: x[1])
    print("Supplier list:")
    for i, supplier in enumerate(sorted_suppliers):
        print(f"{i+1}. Supplier: {supplier[0]}, Supplier code: {supplier[1]}, Tel.No: {supplier[2]}, Address: {supplier[3]}")

def print_hospital_list():
    hospitals = latest_hospitals()
    sorted_hospitals = sorted(hospitals, key=lambda x: x[1])
    print("Hospital list:")
    for i, hospital in enumerate(sorted_hospitals):
        print(f"{i+1}. Hospital: {hospital[0]}, Hospital code: {hospital[1]}, Tel.No: {hospital[2]}, Address: {hospital[3]}")

def print_user_list():
    users = latest_user()
    sorted_users = sorted(users, key=lambda x: x[1])
    print("User list:")
    for i, user in enumerate(sorted_users):
        print(f"{i+1}. Users: {user[0]}, Password: {user[1]}")

def receive_item():
    print_item_list()
    print_supplier_list()
    item_code = input("Enter item code: ").upper().strip()
    if validate_item_code(latest_items(), item_code):
        supplier_code = input("Enter supplier code: ").upper().strip()
        if validate_item_supplier_code(latest_suppliers(), supplier_code):
            try:
                stock = int(input("Enter number of stock to be received: "))
                if validate_item_stock(stock):
                    items = add_items_stock(latest_items(), item_code, stock)
                    write_item(items)
                    print("Item successfully received!\n")
                    item_menu()
                else:
                    print("Invalid item stock. Returning to main menu...\n")
                    item_menu()
            except ValueError:
                print("Invalid item stock. Returning to main menu...\n")
        else:
            print("Invalid supplier code. Returning to main menu...\n")
            item_menu()
    else:
        print("Invalid item code. Returning to main menu...\n")
        item_menu()

def distribute_item():
    print_item_list()
    print_hospital_list()
    item_code = input("Enter item code: ").upper().strip()
    if validate_item_code(latest_items(), item_code):
        hospital_code = input("Enter hospital code: ").upper().strip()
        if validate_item_hospital_code(latest_hospitals(), hospital_code):
            try:
                stock = int(input("Enter number of stock to be distributed: "))
                if validate_item_stock_distribution(stock, item_code):
                    items = minus_items_stock(latest_items(), item_code, stock)
                    write_item(items)
                    print("Item successfully distributed!\n")
                    item_menu()
                else:
                    print("Invalid item stock. Returning to main menu...\n")
                    item_menu()
            except ValueError:
                print("Invalid item stock. Returning to main menu...\n")
                item_menu()
        else:
            print("Invalid hospital code. Returning to main menu...\n")
            item_menu()
    else:
        print("Invalid item code. Returning to main menu...\n")
        item_menu()

# Print Functions
def print_main_menu():
    print("""===================================
        INVENTORY MANAGEMENT
===================================

Main Menu:
1. Item menu
2. Supplier menu
3. Hospital menu
4. Register user
5. Delete user
6. Restart system
7. Exit system

""")

def print_restart_system():
    print("""===================================
INVENTORY MANAGEMENT
===================================

System Initialization:

Would you like to restart the system?

1. Yes
2. No

""")
    
def print_login_page():
    print("""===================================
        INVENTORY MANAGEMENT
===================================

Login Page:

""")

def print_register_page():
    print("""===================================
        INVENTORY MANAGEMENT
===================================

Register User Page:

""")

def print_delete_page():
    print("""===================================
        INVENTORY MANAGEMENT
===================================

Delete User Page:

""")

def print_item_menu():
    print("""===================================
        INVENTORY MANAGEMENT
===================================

Item Menu:
1. Edit item stock
2. Edit item supplier
3. Print item list
4. Print low stock item
5. Receive item
6. Distribute item
7. Main menu

""")

# Validation Functions
def validate_num_user(users):
    return len(users) < 4

def validate_num_attempt(attempts):
    return attempts < 3

def validate_cred_user(users, username, password):
    for user_info in users:
        if username == user_info[0] and password == user_info[1]:
            return True
    return False

def validate_item_choice(choice):
    return 1 <= choice <= 7

def validate_item_code(items, item_code):
    for item in items:
        if item_code == item[1]:
            return True
    return False

def validate_item_stock(item_stock):
    return item_stock >= 0

def validate_item_supplier_code(suppliers, supplier_code):
    for supplier in suppliers:
        if supplier[1] == supplier_code:
            return True
    return False

def validate_item_hospital_code(hospitals, hospital_code):
    for hospital in hospitals:
        if hospital[1] == hospital_code:
            return True
    return False

def validate_main_choice(choice):
    return 1 <= choice <= 7

def validate_restart_system(choice):
    return 1 <= choice <= 2

def validate_item_stock_distribution(stock_minus, item_code):
    items = latest_items()
    for item_info in items:
        if item_info[1] == item_code:
            stock_get_minus = int(item_info[3].split(" ")[0].strip())
    stock_got_minus = stock_get_minus - stock_minus
    return stock_got_minus >= 0

def validate_username(username):
    users = latest_user()
    for user_info in users:
        if user_info[0] == username:
            return False
    return True

# Write Functions
def write_user(users):
    with open("user.txt", "w") as user_file:
        for user_info in users:
            user_file.write(f"User: {user_info[0]}\n")
            user_file.write(f"Password: {user_info[1]}\n")
            user_file.write("\n")

def write_supplier(suppliers):
    with open("supplier.txt", "w") as suppliers_file:
        for supplier in suppliers:
            suppliers_file.write(f"Supplier: {supplier[0]}\n")
            suppliers_file.write(f"Supplier code: {supplier[1]}\n")
            suppliers_file.write(f"Tel.No: {supplier[2]}\n")
            suppliers_file.write(f"Address: {supplier[3]}\n")
            suppliers_file.write("\n")

def write_hospital(hospitals):
    with open("hospital.txt", "w") as hospital_file:
        for hospital in hospitals:
            hospital_file.write(f"Hospital: {hospital[0]}\n")
            hospital_file.write(f"Hospital code: {hospital[1]}\n")
            hospital_file.write(f"Tel.No: {hospital[2]}\n")
            hospital_file.write(f"Address: {hospital[3]}\n")
            hospital_file.write("\n")

def write_item(items):
    with open("ppe.txt", "w") as ppe_file:
        for item in items:
            ppe_file.write(f"Item: {item[0]}\n")
            ppe_file.write(f"Item code: {item[1]}\n")
            ppe_file.write(f"Supplier code: {item[2]}\n")
            ppe_file.write(f"Stock: {item[3]}\n")
            ppe_file.write("\n")

# Data Retrieval Functions
def latest_user():
    users = []
    with open("user.txt", "r") as user_file:
        lines = user_file.readlines()
        user_info = []
        for line in lines:
            line = line.strip()
            if line.startswith("User:"):
                user = line.split(":")[1].strip()
                user_info.append(user)
            elif line.startswith("Password:"):
                user = line.split(":")[1].strip()
                user_info.append(user)
                users.append(user_info)
                user_info = []
    return users

def latest_suppliers():
    suppliers = []
    with open("supplier.txt", "r") as supplier_file:
        lines = supplier_file.readlines()
        supplier_info = []
        for line in lines:
            line = line.strip()
            if line.startswith("Supplier:"):
                supplier = line.split(":")[1].strip()
                supplier_info.append(supplier)
            if line.startswith("Supplier code:"):
                supplier = line.split(":")[1].strip()
                supplier_info.append(supplier)
            if line.startswith("Tel.No:"):
                supplier = line.split(":")[1].strip()
                supplier_info.append(supplier)
            if line.startswith("Address:"):
                supplier = line.split(":")[1].strip()
                supplier_info.append(supplier)
                suppliers.append(supplier_info)
                supplier_info = []
    return suppliers

def latest_hospitals():
    hospitals = []
    with open("hospital.txt", "r") as hospital_file:
        lines = hospital_file.readlines()
        hospital_info = []
        for line in lines:
            line = line.strip()
            if line.startswith("Hospital:"):
                hospital = line.split(":")[1].strip()
                hospital_info.append(hospital)
            if line.startswith("Hospital code:"):
                hospital = line.split(":")[1].strip()
                hospital_info.append(hospital)
            if line.startswith("Tel.No:"):
                hospital = line.split(":")[1].strip()
                hospital_info.append(hospital)
            if line.startswith("Address:"):
                hospital = line.split(":")[1].strip()
                hospital_info.append(hospital)
                hospitals.append(hospital_info)
                hospital_info = []
    return hospitals

def latest_items():
    items = []
    with open("ppe.txt", "r") as ppe_file:
        lines = ppe_file.readlines()
        item_info = []
        for line in lines:
            line = line.strip()
            if line.startswith("Item:"):
                item = line.split(":")[1].strip()
                item_info.append(item)
            elif line.startswith("Item code:"):
                item = line.split(":")[1].strip()
                item_info.append(item)
            elif line.startswith("Supplier code:"):
                item = line.split(":")[1].strip()
                item_info.append(item)
            elif line.startswith("Stock: "):
                item = line.split(":")[1].strip()
                item_info.append(item)
                items.append(item_info)
                item_info = []
    return items


# Stock Management Functions
def add_items_stock(items, item_code, item_stock):
    for item in items:
        if item_code == item[1]:
            item_stock = int(item[3].split(" ")[0]) + item_stock
            item[3] = f"{item_stock} boxes"
    return items

def minus_items_stock(items, item_code, item_stock):
    for item in items:
        if item_code == item[1]:
            item_stock = int(item[3].split(" ")[0]) - item_stock
            item[3] = f"{item_stock} boxes"
    return items

def change_items_stock(items, item_code, item_stock):
    for item in items:
        if item_code == item[1]:
            item[3] = f"{item_stock} boxes"
    return items

def change_items_supplier(items, item_code, supplier_code):
    for item in items:
        if item_code == item[1]:
            item[2] = supplier_code
    return items

# Initialize the system
restart_system_menu()
