import database


while True:
    print("////////////////////////////")
    print("        Welcome             ")
    print("////////////////////////////")
    choice = eval(input('1. Create account 2. Login 3. Quit : '))
    if choice == 1:
        username = input('Create username: ')
        password = input('Create password: ')
        database.add_user(username,password)
        print('Account created')
    elif choice == 2:
        database.login()
        print("Login succees")
        break
    elif choice == 3:
        break

        print("////////////////////////////")
        print("       Thank you            ")
        print("////////////////////////////")

