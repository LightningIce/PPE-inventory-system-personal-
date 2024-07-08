# Main Menu Functions
def main_menu():
    print_main_menu()
    while True:
        try:
            choice = int(input("Please select an option (1-8): "))
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
        report_menu()
    elif choice == 5:
        print_user_list()
        register()
    elif choice == 6:
        print_user_list()
        delete()
    elif choice == 7:
        restart_system()
        main_menu()
    elif choice == 8:
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
    print_supplier_menu()
    while True:
        try:
            choice = int(input("Please select an option (1-5): "))
            if not validate_supplier_choice(choice):
                print("Please enter a valid number.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue
        break
    if choice == 1:
        edit_supplier_name()
    elif choice == 2:
        edit_supplier_telephone()
    elif choice == 3:
        edit_supplier_address()
    elif choice == 4:
        print_supplier_list()
        supplier_menu()
    elif choice == 5:
        main_menu()

def hospital_menu():
    print_hospital_menu()
    while True:
        try:
            choice = int(input("Please select an option (1-5): "))
            if not validate_hospital_choice(choice):
                print("Please enter a valid number.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue
        break
    if choice == 1:
        edit_hospital_name()
    elif choice == 2:
        edit_hospital_telephone()
    elif choice == 3:
        edit_hospital_address()
    elif choice == 4:
        print_hospital_list()
        hospital_menu()
    elif choice == 5:
        main_menu()

def report_menu():
    print_report_menu()
    while True:
        try:
            choice = int(input("Please select an option (1-5): "))
            if not validate_report_choice(choice):
                print("Please enter a valid number.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue
        break
    if choice == 1:
        search_item_distribution()
    elif choice == 2:
        print_supplier_ppe_list()
    elif choice == 3:
        print_hospital_ppe_distribution()
    elif choice == 4:
        print_monthly_transaction_report()
    elif choice == 5:
        main_menu()

# System Restart Function
def restart_system():
    users = [["admin", "admin"]]
    suppliers = [
        ["Supplier A", "A", "0123456789", "22, Jalan TPP 2/2, Taman Perindustrian Puchong, 47100 Puchong, Selangor."],
        ["Supplier B", "B", "0129876543", "30-2, Jalan Harmoni 1, Balakong, 43300 Seri Kembangan, Selangor."],
        ["Supplier C", "C", "0134567890", "28 GF, Jalan 15/2, Seksyen 15, 43650 Bandar Baru Bangi, Selangor."],
        ["Supplier D", "D", "0145678901", "No.20, Jalan Bayi Tinggi 3, KS6, Batu Unjur, 41200 Klang, Selangor."]
    ]
    hospitals = [
        ["Hospital A", "A", "0156789012", "Jalan Raja, 50588 Kuala Lumpur, Wilayah Persekutuan Kuala Lumpur."],
        ["Hospital B", "B", "0167890123", "2, Jalan 2/96b, Taman Cheras Indah, 56100 Kuala Lumpur, Wilayah Persekutuan Kuala Lumpur."],
        ["Hospital C", "C", "0178901234", "Lot 70, 14 Jalan 14/7, Seksyen 14, 46300 Petaling Jaya, Selangor."],
        ["Hospital D", "D", "0189012345", "2, Jalan Mamanda 10, Taman Dato Ahmad Said, 68000 Ampang, Selangor."]
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

def print_user_list():
    users = latest_user()
    sorted_users = sorted(users, key=lambda x: x[1])
    print("User list:")
    for i, user in enumerate(sorted_users):
        print(f"{i+1}. Users: {user[0]}, Password: {user[1]}")

# Item Management Functions
def edit_item_stock():
    print_item_list()
    item_code = input("Enter item code: ").upper().strip()
    if validate_item_code(latest_items(), item_code):
        try:
            item_stock = int(input("Enter new item stock: "))
            if validate_item_stock(item_stock):
                items = change_items_stock(latest_items(), item_code, item_stock)
                write_item(items)
                print("Item stock updated successfully!")
                item_menu()
            else:
                print("Invalid item stock. Returning to item menu...\n")
                item_menu()
        except ValueError:
            print("Invalid item stock. Returning to item menu...\n")
            item_menu()
    else:
        print("Invalid item code. Returning to item menu...\n")
        item_menu()

def edit_item_supplier():
    print_item_list()
    item_code = input("Enter item code: ").upper().strip()
    if validate_item_code(latest_items(), item_code):
        supplier_code = input("Enter new supplier code: ").upper().strip()
        if validate_supplier_code(latest_suppliers(), supplier_code):
            items = change_items_supplier(latest_items(), item_code, supplier_code)
            write_item(items)
            print("Item's supplier code updated successfully!\n")
            item_menu()
        else:
            print("Invalid supplier code. Returning to item menu...\n")
            item_menu()
    else:
        print("Invalid item code. Returning to item menu...\n")
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

def receive_item():
    print_item_list()
    print_supplier_list()
    item_code = input("Enter item code: ").upper().strip()
    if validate_item_code(latest_items(), item_code):
        supplier_code = input("Enter supplier code: ").upper().strip()
        if validate_supplier_code(latest_suppliers(), supplier_code):
            try:
                stock = int(input("Enter number of stock to be received: "))
                if validate_item_stock(stock):
                    items = add_items_stock(latest_items(), item_code, stock)
                    write_item(items)
                    record_received_items(item_code, supplier_code, stock)
                    print("Item successfully received!\n")
                    item_menu()
                else:
                    print("Invalid item stock. Returning to item menu...\n")
                    item_menu()
            except ValueError:
                print("Invalid item stock. Returning to item menu...\n")
        else:
            print("Invalid supplier code. Returning to item menu...\n")
            item_menu()
    else:
        print("Invalid item code. Returning to item menu...\n")
        item_menu()

def distribute_item():
    print_item_list()
    print_hospital_list()
    item_code = input("Enter item code: ").upper().strip()
    if validate_item_code(latest_items(), item_code):
        hospital_code = input("Enter hospital code: ").upper().strip()
        if validate_hospital_code(latest_hospitals(), hospital_code):
            try:
                stock = int(input("Enter number of stock to be distributed: "))
                if validate_item_stock_distribution(stock, item_code):
                    items = minus_items_stock(latest_items(), item_code, stock)
                    write_item(items)
                    record_distributed_items(item_code, hospital_code, stock)
                    print("Item successfully distributed!\n")
                    item_menu()
                else:
                    print("Invalid item stock. Returning to item menu...\n")
                    item_menu()
            except ValueError:
                print("Invalid item stock. Returning to item menu...\n")
                item_menu()
        else:
            print("Invalid hospital code. Returning to item menu...\n")
            item_menu()
    else:
        print("Invalid item code. Returning to item menu...\n")
        item_menu()

# Supplier Management Functions
def edit_supplier_name():
    print_supplier_list()
    supplier_code = input("Enter supplier code: ").strip().upper()
    if validate_supplier_code(latest_suppliers(), supplier_code):
        new_supplier_name = input("Enter new supplier name: ")
        suppliers = change_supplier_name(supplier_code, new_supplier_name)
        write_supplier(suppliers)
        print("Supplier successfully distributed!\n")
        supplier_menu()
    else:
        print("Invalid supplier code. Returning to supplier menu...\n")
        supplier_menu()

def edit_supplier_telephone():
    print_supplier_list()
    supplier_code = input("Enter supplier code: ").strip().upper()
    if validate_supplier_code(latest_suppliers(), supplier_code):
        new_supplier_telephone = input("Enter new supplier telephone: ")
        if validate_telephone(new_supplier_telephone):
            suppliers = change_supplier_telephone(supplier_code, new_supplier_telephone)
            write_supplier(suppliers)
            print("Supplier successfully distributed!\n")
            supplier_menu()
        else:
            print("Invalid phone number. Returning to supplier menu...\n")
            supplier_menu()
    else:
        print("Invalid supplier code. Returning to supplier menu...\n")
        supplier_menu()

def edit_supplier_address():
    print_supplier_list()
    supplier_code = input("Enter supplier code: ").strip().upper()
    if validate_supplier_code(latest_suppliers(), supplier_code):
        new_supplier_address = input("Enter new supplier address: ")
        suppliers = change_supplier_address(supplier_code, new_supplier_address)
        write_supplier(suppliers)
        print("Supplier successfully distributed!\n")
        supplier_menu()
    else:
        print("Invalid supplier code. Returning to supplier menu...\n")
        supplier_menu()

def print_supplier_list():
    suppliers = latest_suppliers()
    sorted_suppliers = sorted(suppliers, key=lambda x: x[1])
    print("Supplier list:")
    for i, supplier in enumerate(sorted_suppliers):
        print(f"{i+1}. Supplier: {supplier[0]}, Supplier code: {supplier[1]}, Tel.No: {supplier[2]}, Address: {supplier[3]}")

# Hospital Management Functions
def edit_hospital_name():
    print_hospital_list()
    hospital_code = input("Enter hospital code: ").strip().upper()
    if validate_hospital_code(latest_hospitals(), hospital_code):
        new_hospital_name = input("Enter new hospital name: ")
        hospitals = change_hospital_name(hospital_code, new_hospital_name)
        write_hospital(hospitals)
        print("hospital successfully distributed!\n")
        hospital_menu()
    else:
        print("Invalid hospital code. Returning to hospital menu...\n")
        hospital_menu()

def edit_hospital_telephone():
    print_hospital_list()
    hospital_code = input("Enter hospital code: ").strip().upper()
    if validate_hospital_code(latest_hospitals(), hospital_code):
        new_hospital_telephone = input("Enter new hospital telephone: ")
        if validate_telephone(new_hospital_telephone):
            hospitals = change_hospital_telephone(hospital_code, new_hospital_telephone)
            write_hospital(hospitals)
            print("hospital successfully distributed!\n")
            hospital_menu()
        else:
            print("Invalid phone number. Returning to hospital menu...\n")
    else:
        print("Invalid hospital code. Returning to hospital menu...\n")
        hospital_menu()

def edit_hospital_address():
    print_hospital_list()
    hospital_code = input("Enter hospital code: ").strip().upper()
    if validate_hospital_code(latest_hospitals(), hospital_code):
        new_hospital_address = input("Enter new hospital address: ")
        hospitals = change_hospital_address(hospital_code, new_hospital_address)
        write_hospital(hospitals)
        print("hospital successfully distributed!\n")
        hospital_menu()
    else:
        print("Invalid hospital code. Returning to hospital menu...\n")
        hospital_menu()

def print_hospital_list():
    hospitals = latest_hospitals()
    sorted_hospitals = sorted(hospitals, key=lambda x: x[1])
    print("Hospital list:")
    for i, hospital in enumerate(sorted_hospitals):
        print(f"{i+1}. Hospital: {hospital[0]}, Hospital code: {hospital[1]}, Tel.No: {hospital[2]}, Address: {hospital[3]}")

# Report Management Functions
def search_item_distribution():
    print_item_list()
    item_code = input("Enter item code to search: ").strip().upper()
    if validate_item_code(latest_items(), item_code):
        print_search_item_distribution(item_code)
        report_menu()
    else:
        print("Invalid item code. Returning to report menu...\n")
        report_menu()

def print_supplier_ppe_list():
    items = latest_items()
    suppliers = latest_suppliers()
    
    supplier_name_ppe_items = []
    
    for supplier in suppliers:
        supplier_name = supplier[0]
        supplier_code = supplier[1]
        supplied_items = []
        
        for item in items:
            if item[2] == supplier_code:
                supplied_items.append(item[0])
            
                if [supplier_name, supplied_items] not in supplier_name_ppe_items:
                    supplier_name_ppe_items.append([supplier_name, supplied_items])

            
    print("List of Suppliers and PPE items Supplied:")
    for supplier_info in supplier_name_ppe_items:
        print(f"Supplier: {supplier_info[0]}")
        print(f"Items: {', '.join(supplier_info[1])}")
        print()
    report_menu()

def print_hospital_ppe_distribution():
    distributed_items = latest_distributed_items()
    hospitals = latest_hospitals()
    items = latest_items()

    hospital_items_distribution = []

    for hospital in hospitals:
        hospital_name = hospital[0]
        hospital_code = hospital[1]
        distributed_items_to_hospital = {}

        for item in distributed_items:
            if item[2] == hospital_code:
                item_name = [i[0] for i in items if i[1] == item[1]][0]
                item_quantity = int(item[3].split(" ")[0].strip())

                if item_name in distributed_items_to_hospital:
                    distributed_items_to_hospital[item_name] += item_quantity
                else:
                    distributed_items_to_hospital[item_name] = item_quantity

        hospital_items_distribution.append([hospital_name, distributed_items_to_hospital])

    print("List of Hospitals and Distributed Items:")
    for hospital_info in hospital_items_distribution:
        items_str = ", ".join([f"{item}: {quantity}" for item, quantity in hospital_info[1].items()])
        print(f"Hospital: {hospital_info[0]}, Items: {items_str}")
    
    report_menu()

def print_monthly_transaction_report():
    import datetime

    def filter_items_by_month(items, month):
        filtered_items = []
        for item in items:
            item_date = datetime.datetime.strptime(item[0], "%d-%m-%Y")
            if item_date.strftime("%m-%Y") == month:
                filtered_items.append(item)
        return filtered_items

    month = input("Enter month for report (e.g., 06-2024): ")
    received_items = filter_items_by_month(latest_received_items(), month)
    distributed_items = filter_items_by_month(latest_distributed_items(), month)

    received_summary = {}
    for item in received_items:
        supplier_code = item[2]
        item_name = next((i[0] for i in latest_items() if i[1] == item[1]), None)
        quantity = int(item[3].split(" ")[0].strip())
        if supplier_code not in received_summary:
            received_summary[supplier_code] = {}
        if item_name not in received_summary[supplier_code]:
            received_summary[supplier_code][item_name] = 0
        received_summary[supplier_code][item_name] += quantity

    distributed_summary = {}
    for item in distributed_items:
        hospital_code = item[2]
        item_name = next((i[0] for i in latest_items() if i[1] == item[1]), None)
        quantity = int(item[3].split(" ")[0].strip())
        if hospital_code not in distributed_summary:
            distributed_summary[hospital_code] = {}
        if item_name not in distributed_summary[hospital_code]:
            distributed_summary[hospital_code][item_name] = 0
        distributed_summary[hospital_code][item_name] += quantity

    print(f"Overall Transaction Report for {month}:")
    
    print("Supplies Received:")
    for supplier, items in received_summary.items():
        for item, quantity in items.items():
            print(f"Supplier: {supplier}, Item: {item}, Quantity: {quantity}")

    print("\nSupplies Distributed:")
    for hospital, items in distributed_summary.items():
        for item, quantity in items.items():
            print(f"Hospital: {hospital}, Item: {item}, Quantity: {quantity}")

    print()

    report_menu()


# Print Functions
def print_main_menu():
    print("""===================================
        INVENTORY MANAGEMENT
===================================

Main Menu:
1. Item menu
2. Supplier menu
3. Hospital menu
4. Report menu
5. Register user
6. Delete user
7. Restart system
8. Exit system

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

def print_supplier_menu():
    print("""===================================
        INVENTORY MANAGEMENT
===================================

Supplier Menu:
1. Edit supplier name
2. Edit supplier telephone
3. Edit supplier address
4. Print supplier list
5. Main menu

""")

def print_hospital_menu():
    print("""===================================
        INVENTORY MANAGEMENT
===================================

Hospital Menu:
1. Edit hospital name
2. Edit hospital telephone
3. Edit hospital address
4. Print hospital list
5. Main menu

""")

def print_report_menu():
    print("""===================================
        INVENTORY MANAGEMENT
===================================

Report Menu:
1. Search item distribution
2. Print supplier PPE list
3. Print hospital PPE distribution
4. Print monthly transaction report
5. Main menu

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

def validate_supplier_code(suppliers, supplier_code):
    for supplier in suppliers:
        if supplier[1] == supplier_code:
            return True
    return False

def validate_hospital_code(hospitals, hospital_code):
    for hospital in hospitals:
        if hospital[1] == hospital_code:
            return True
    return False

def validate_main_choice(choice):
    return 1 <= choice <= 8

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

def validate_supplier_choice(choice):
    return 1 <= choice <= 5

def validate_hospital_choice(choice):
    return 1 <= choice <= 5

def validate_telephone(phone_number):
    import re
    pattern = r"^\d{10,15}$"
    return bool(re.match(pattern, phone_number))

def validate_report_choice(choice):
    return 1 <= choice <= 5
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

def write_receiving(received_items):
    with open("receiving.txt", "w") as receiving_file:
        for received_item in received_items:
            receiving_file.write(f"Date: {received_item[0]}\n")
            receiving_file.write(f"Item code: {received_item[1]}\n")
            receiving_file.write(f"Supplier code: {received_item[2]}\n")
            receiving_file.write(f"Stock: {received_item[3]}\n")
            receiving_file.write("\n")

def write_distribution(distributed_items):
    with open("distribution.txt", "w") as distribution_file:
        for distributed_item in distributed_items:
            distribution_file.write(f"Date: {distributed_item[0]}\n")
            distribution_file.write(f"Item code: {distributed_item[1]}\n")
            distribution_file.write(f"Hospital code: {distributed_item[2]}\n")
            distribution_file.write(f"Stock: {distributed_item[3]}\n")
            distribution_file.write("\n")

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
            elif line.startswith("Stock:"):
                item = line.split(":")[1].strip()
                item_info.append(item)
                items.append(item_info)
                item_info = []
    return items

def latest_received_items():
    received_items = []
    with open("receiving.txt", "r") as received_items_file:
        lines = received_items_file.readlines()
        received_item_info = []
        for line in lines:
            line = line.strip()
            if line.startswith("Date:"):
                received_item = line.split(":")[1].strip()
                received_item_info.append(received_item)
            elif line.startswith("Item code:"):
                received_item = line.split(":")[1].strip()
                received_item_info.append(received_item)
            elif line.startswith("Suppplier code:"):
                received_item = line.split(":")[1].strip()
                received_item_info.append(received_item)
            elif line.startswith("Stock:"):
                received_item = line.split(":")[1].strip()
                received_item_info.append(received_item)
                received_items.append(received_item_info)
                received_item_info = []
    return received_items

def latest_distributed_items():
    distributed_items = []
    with open("distribution.txt", "r") as distributed_items_file:
        lines = distributed_items_file.readlines()
        distributed_item_info = []
        for line in lines:
            line = line.strip()
            if line.startswith("Date:"):
                distributed_item = line.split(":")[1].strip()
                distributed_item_info.append(distributed_item)
            elif line.startswith("Item code:"):
                distributed_item = line.split(":")[1].strip()
                distributed_item_info.append(distributed_item)
            elif line.startswith("Hospital code:"):
                distributed_item = line.split(":")[1].strip()
                distributed_item_info.append(distributed_item)
            elif line.startswith("Stock:"):
                distributed_item = line.split(":")[1].strip()
                distributed_item_info.append(distributed_item)
                distributed_items.append(distributed_item_info)
                distributed_item_info = []
    return distributed_items


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

# Supplier Detail Management Functions
def change_supplier_name(supplier_code, new_supplier_name):
    suppliers = latest_suppliers()
    for supplier_info in suppliers:
        if supplier_code == supplier_info[1]:
            supplier_info[0] = new_supplier_name
    return suppliers

def change_supplier_telephone(supplier_code, new_supplier_telephone):
    suppliers = latest_hospitals()
    for supplier_info in suppliers:
        if supplier_code == supplier_info[1]:
            supplier_info[2] = new_supplier_telephone
    return suppliers

def change_supplier_address(supplier_code, new_supplier_address):
    suppliers = latest_suppliers()
    for supplier_info in suppliers:
        if supplier_code == supplier_info[1]:
            supplier_info[3] = new_supplier_address
    return suppliers

# Hospital Detail Management Functions
def change_hospital_name(hospital_code, new_hospital_name):
    hospitals = latest_hospitals()
    for hospital_info in hospitals:
        if hospital_code == hospital_info[1]:
            hospital_info[0] = new_hospital_name
    return hospitals

def change_hospital_telephone(hospital_code, new_hospital_telephone):
    hospitals = latest_hospitals()
    for hospital_info in hospitals:
        if hospital_code == hospital_info[1]:
            hospital_info[2] = new_hospital_telephone
    return hospitals

def change_hospital_address(hospital_code, new_hospital_address):
    hospitals = latest_hospitals()
    for hospital_info in hospitals:
        if hospital_code == hospital_info[1]:
            hospital_info[3] = new_hospital_address
    return hospitals

# Record Detail Management Functions
def record_received_items(item_code, supplier_code, num_stock):
    import datetime
    received_items = latest_received_items()
    received_items_info = []
    
    current_date = datetime.datetime.now().strftime("%d-%m-%Y")
    received_items_info.append(current_date)
    received_items_info.append(item_code)
    received_items_info.append(supplier_code)
    received_items_info.append(f"{num_stock} boxes")
    
    received_items.append(received_items_info)
    write_receiving(received_items)

def record_distributed_items(item_code, hospital_code, num_stock):
    import datetime
    distributed_items = latest_distributed_items()
    distributed_items_info = []
    
    current_date = datetime.datetime.now().strftime("%d-%m-%Y")
    distributed_items_info.append(current_date)
    distributed_items_info.append(item_code)
    distributed_items_info.append(hospital_code)
    distributed_items_info.append(f"{num_stock} boxes")
    
    distributed_items.append(distributed_items_info)
    write_distribution(distributed_items)

def print_search_item_distribution(item_code):
    distributed_items = latest_distributed_items()
    distribution_summary = []
    
    for item in distributed_items:
        if item[1] == item_code:
            hospital_code = item[2]
            quantity = int(item[3].split(" ")[0].strip())
            found = False
            for summary in distribution_summary:
                if summary[0] == hospital_code:
                    summary[1] += quantity
                    found = True
                    break
            if not found:
                distribution_summary.append([hospital_code, quantity])
                
    print(f"Distribution list for item code {item_code}:")
    for summary in distribution_summary:
        print(f"Hospital code: {summary[0]}")
        print(f"Quantity: {summary[1]}\n")

# Initialize the system
restart_system_menu()
