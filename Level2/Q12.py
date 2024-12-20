def create_login_system():
    stored_username = ""
    stored_password = ""
    
    def register():
        nonlocal stored_username, stored_password
        username = input("Enter username: ")
        attempts = 3
        while attempts > 0:
            password = input("Enter password: ")
            confirm_password = input("Re-type password: ")
            if password == confirm_password:
                stored_username = username
                stored_password = password
                print("Registration successful!")
                return True
            else:
                attempts -= 1
                if attempts > 0:
                    print(f"Passwords don't match! {attempts} attempts remaining.")
                else:
                    print("Registration failed. Too many incorrect password attempts.")
        return False
    
    def login():
        nonlocal stored_username, stored_password
        username = input("Enter username: ")
        if username != stored_username:
            print("Username not found.")
            return False
        attempts = 3
        while attempts > 0:
            password = input("Enter password: ")
            if password == stored_password:
                print("Login successful!")
                return True
            else:
                attempts -= 1
                if attempts > 0:
                    print(f"Incorrect password. {attempts} attempts remaining.")
                else:
                    print("Login failed. Too many incorrect attempts.")
        return False
    
    return register, login


if __name__ == "__main__":
    register, login = create_login_system()
    if register():
        if login():
            print("Welcome!")
        else:
            print("Access denied.")
    else:
        print("Registration failed. Cannot proceed to login.")