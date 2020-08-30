auser = 'admin'
apasswd = 'admin'
username = []
password = []
run = True

while run:
    print("////////////////////////////")
    print("        Welcome             ")
    print("////////////////////////////")
    choice = eval(input('1. Log in 2. Create account 3. Quit : '))
    if choice == 1:
        name = input('Enter user name: ')
        if name == username:
            pin = input('Enter password: ')
            if pin == password:
                print("Access Granted")
            else:
                print("Access Deined")
        else:
            print("Username name not found")
    elif choice == 2:
        temp = input('Create username: ')
        username.append(temp)
        temp2 = input('Enter password: ')
        confirm = input('Re-type password: ')
        if temp2 == confirm:
            print("Account for ",username , "created")
        else:
            print("Password dont match")
    elif choice == 3:
        run = False

        print("////////////////////////////")
        print("       Thank you            ")
        print("////////////////////////////")

