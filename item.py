import main
import supplier
import hospital


def item_menu():
    print_item_menu()
    while True:
        try:
            choice = int(input("Please select an option (1-7): "))
            print()
            if not validate_item_choice(choice):
                print("Please enter a valid number.")
                print()
                continue
        except:
            print("Please enter a valid number.")
            print()
            continue
        break
    if choice == 1:
        edit_item_stock()
    elif choice == 2:
        edit_item_supplier()
    elif choice == 3:
        print_item_list(latest_items())
    elif choice == 4:
        print_low_stock_item(latest_items())
    elif choice == 5:
        receive_item()
    elif choice == 6:
        distribute_item()
    elif choice == 7:
        main.main_menu()


def edit_item_stock():
    print_item_list()
    item_code = input("Enter item code:").upper().strip()
    
    if validate_item_code(latest_items(), item_code):
        item_stock = int(input("Enter new item stock: "))
        try:
            if validate_item_stock(item_stock):
                items = change_items_stock(latest_items(), item_code, item_stock)
                write_item(items)
                print("Item stock updated successfully!\n\n\n")
                main.main_menu()
            else:
                print("Invalid item stock. Returning to main menu...\n\n\n")
                main.main_menu()
        except:
            print("Invalid item stock. Returning to main menu...\n\n\n")
            main.main_menu()
    else:
        print("Invalid item code. Returning to main menu...\n\n\n")
        main.main_menu()


def edit_item_supplier():
    print_item_list()
    item_code = input("Enter item code: ").upper().strip()
    
    if validate_item_code(latest_items(), item_code):
        supplier_code = input("Enter new supplier code: ").upper().strip()
        if validate_item_supplier_code(supplier.latest_suppliers(), supplier_code):
            items = change_items_stock(latest_items(), item_code, supplier_code)
            write_item(items)
            print("Item's supplier code updated successfully!\n\n\n")
            main.main_menu()
        else:
            print("Invalid supplier code. Returning to main menu...\n\n\n")
            main.main_menu()
    else:
        print("Invalid item code. Returning to main menu...\n\n\n")
        main.main_menu()


def print_item_list(items):
    sorted_items = sorted(items, key=lambda x: x[1])
    
    print("Available items:")
    for i, item in enumerate(sorted_items):
        print(f"{i+1}. Item: {item[0]}, Item code: {item[1]}, Supplier code: {item[2]}, Stock: {item[3]}")
    print()


def print_low_stock_item(items):
    sorted_items = sorted(items, key=lambda x: x[3])
    
    print("Low stock item:")
    i = 1
    for item in sorted_items:
        stock = int(item[3].split(" ")[1].strip())
        if stock < 25:
            print(print(f"{i}. Item: {item[0]}, Item code: {item[1]}, Supplier code: {item[2]}, Stock: {item[3]}"))
            i += 1
    print()


def receive_item():
    print_item_list()
    supplier.print_supplier_list()
    item_code = input("Enter item code: ").upper().strip()
    if validate_item_code(latest_items(), item_code):
        supplier_code = input("Enter supplier code: ").upper().strip()
        if validate_item_supplier_code(supplier.latest_supplier(), supplier_code):
            stock = input("Enter number of stock to be received: ")
            try:
                if validate_item_stock(stock):
                    items = add_items_stock(latest_items(), item_code, stock)
                    write_item(items)
                    print("Item successfully received!\n\n\n")
                    main.main_menu()
                else:
                    print("Invalid item stock. Returning to main menu...\n\n\n")
                    main.main_menu()
            except:
                print("Invalid item stock. Returning to main menu...\n\n\n")
                main.main_menu()
        else:
            print("Invalid supplier code. Returning to main menu...\n\n\n")
            main.main_menu()
    else:
        print("Invalid item code. Returning to main menu...\n\n\n")
        main.main_menu()


def distribute_item():
    print_item_list()
    hospital.print_hospital_list()
    item_code = input("Enter item code: ").upper().strip()
    
    if validate_item_code(latest_items(), item_code):
        hospital_code = input("Enter hospital code: ").upper().strip()
        if validate_item_hospital_code(hospital.latest_hospital(), hospital_code):
            stock = input("Enter number of stock to be distributed: ")
            try:
                if validate_item_stock(stock):
                    items = minus_items_stock(latest_items(), item_code, stock)
                    write_item(items)
                    print("Item successfully distributed!\n\n\n")
                    main.main_menu()
                else:
                    print("Invalid item stock. Returning to main menu...\n\n\n")
                    main.main_menu()
            except:
                print("Invalid item stock. Returning to main menu...\n\n\n")
                main.main_menu()
        else:
            print("Invalid supplier code. Returning to main menu...\n\n\n")
            main.main_menu()
    else:
        print("Invalid item code. Returning to main menu...\n\n\n")
        main.main_menu()


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


def validate_item_choice(choice):
    if 1 <= choice <= 7:
        return True
    return False


def validate_item_code(items, item_code):
    for item in items:
        if item_code == item[1]:
            return True
    return False


def validate_item_stock(item_stock):
    if item_stock < 0:
        return False
    return True


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


def add_items_stock(items, item_code, item_stock):
    for item in items:
        if item_code == item[1]:
            item_stock = item[3] + item_stock
            item[3] = f"{item_stock} box"
    return items


def minus_items_stock(items, item_code, item_stock):
    for item in items:
        if item_code == item[1]:
            item_stock = item[3] - item_stock
            item[3] = f"{item_stock} box"
    return items


def change_items_stock(items, item_code, item_stock):
    for item in items:
        if item_code == item[1]:
            item[3] = f"{item_stock} box"
    return items


def change_items_supplier(items, item_code, supplier_code):
    for item in items:
        if item_code == item[1]:
            item[2] = supplier_code
    return items

def write_item(items):
    ppe_file = open("ppe.txt", "w")
    for item in items:
        ppe_file.write(f"Item: {item[0]}")
        ppe_file.write(f"Item code: {item[1]}")
        ppe_file.write(f"Supplier code: {item[2]}")
        ppe_file.write(f"Stock: {item[3]}")
        ppe_file.write()
    ppe_file.close()


def latest_items():
    items = []
    item_info = []
    ppe_file = open("ppe.txt", "r")
    lines = ppe_file.readlines()
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
    ppe_file.close()
    return items