import hospital
import item
import login
import report
import supplier

def main_menu():
    print_main_menu()
    
    while True:
        try:
            choice = int(input("Please select an option (1-7): "))
            if not validate_main_choice(choice):
                print("Please enter a valid number.")
                continue
        except:
            print("Please enter a valid number.")
            continue
        break
    if choice == 1:
        item.item_menu()
    elif choice == 2:
        supplier.supplier_menu()
    elif choice == 3:
        hospital.hospital_menu()
    elif choice == 4:
        login.register()
    elif choice == 5:
        login.delete()
    elif choice == 6:
        restart_system()
    elif choice == 7:
        exit()
    


def main():
    login.login()


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

def validate_main_choice(choice):
    if 1 <= choice <= 7:
        return True
    return False


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
    item = [
    ["Head cover", "HC", "A", "100 boxes"],
    ["Face shield", "FS", "MOD", "100 boxes"],
    ["Mask", "MS", "SFL", "100 boxes"],
    ["Gloves", "GL", "BES", "100 boxes"],
    ["Gown", "GW", "MOD", "100 boxes"],
    ["Shoe covers", "SC", "SFL", "100 boxes"]
    ]
    
    login.write_user(users)
    supplier.write_supplier(suppliers)
    hospital.write_hospital(hospitals)
    item.write_item(item)
    
    distribution_file = open("distribution.txt", "w")
    distribution_file.close()
    receiving_file = open("receiving.txt", "w")
    receiving_file.close()
    



if __name__ == "__main__":
    main()