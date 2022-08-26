username = "python"
password = "rules"
loginAttempts = 0

while True:

    userUsername = input("Enter your username: ")
    userPassword = input("Enter your password: ")
    loginAttempts = loginAttempts + 1

    if userUsername == username and userPassword == password:
        print("Welcome")
        break

    elif loginAttempts == 5:
        print("Access denied.")
        break

    else:
        continue


