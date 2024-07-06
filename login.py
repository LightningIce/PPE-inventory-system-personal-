import main

def login():
    num_attempts = 0
    while True:
        if validate_num_attempt(num_attempts):
            exit()
            
        print_login_page()
        
        username = input("Enter Username to login: ").strip()
        password = input("Enter Password to login: ").strip()
        print()
        
        if validate_cred_user(latest_user(), username, password):
            print("Login Successful!")
            print()
            main.main_menu()
        else:
            print("Invalid username or password.")
            print()
            num_attempts += 1


def register():
    if validate_num_user():
        print_register_page()

        username = input("Enter Username to register: ").strip()
        password = input("Enter Password to register: ").strip()
        print()
        
        users = add_user(latest_user(), username, password)
        write_user(users)
        
        main.main_menu()
    else:
        print("MAX USER REACHED")
        print()
        main.main_menu()


def delete_user():
    print_delete_page()
    
    username = input("Enter Username to delete user: ").strip()
    password = input("Enter Password to delete user: ").strip()
    print()
    
    if validate_cred_user:
        users = delete_user(latest_user(), username, password)
        write_user(users)
        main.main_menu()
    else:
        print("USER NOT FOUND")
        print()
        main.main_menu()


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


def validate_num_user(users):
    if len(users) == 4:
        return False
    else:
        return True


def validate_num_attempt(attempts):
    if attempts == 3:
        return False
    else:
        return True


def validate_cred_user(users, username, password):
    for user_info in users:
        if username == user_info[0] and password == user_info[1]:
            return True
    return False


def add_user(users, username, password):
    user_info = [username, password]
    users.append(user_info)
    return users


def delete_user(users, username, password):
    for user_info in users:
        if username == user_info[0] and password == user_info[1]:
            users.remove(user_info)
    return users


def latest_user():
    user_file = open("user.txt", "r")
    lines = user_file.readlines()
    users = []
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
    user_file.close()
    return users


def write_user(users):
    user_file = open("user.txt", "w")
    for user_info in users:
        user_file.writelines(f"User: {user_info[0]}")
        user_file.writelines(f"Password: {user_info[1]}")
        user_file.writelines()
    user_file.close()

