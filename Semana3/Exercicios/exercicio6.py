while True:
    username = input("Type in your username: ")
    pwd = input("Type in your password: ")
    if pwd == username:
        print("The login credentials are invalid.")
    else:
        print("Login successful.")
        break