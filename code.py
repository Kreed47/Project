def Buy(name):
    with open("Users.txt", "r+") as f1:
        users = f1.readlines()
        for user in users:
            if name in user:
                data = user.strip().split(",")
                with open("Stocks.txt", "r+") as f2:
                    stock_name = input("Enter name of stock to purchase: ")
                    stocks = f2.readlines()                    
                    found = False
                    for stock in stocks:
                        if stock_name in stock:
                            found = True
                            stock_data = stock.strip().split(",")
                            if int(stock_data[1]) < 0:
                                print("Stocks are out")
                                exit()
                            if int(data[3]) < int(stock_data[2]):
                                print("Insufficient funds")
                                exit()
                            stock_data[1] = str(int(stock_data[1]) - 1)
                            stocks.remove(stock)
                            stocks.insert(0, ",".join(stock_data) + "\n")
                            data[3] = str(int(data[3]) - int(stock_data[2]))
                            data[4] = str(int(data[4]) + 1)
                            users.remove(user)
                            users.insert(0, ",".join(data) + "\n")
                    if not found:
                        print("Stock not found")
                        exit()
                    f2.seek(0)
                    f2.truncate()
                    for stock in stocks:
                        f2.write(stock)
                f1.seek(0)
                f1.truncate()
                for user in users:
                    f1.write(user)


def Sell(name):
    with open("Users.txt", "r+") as f1:
        users = f1.readlines()
        for user in users:
            if name in user:
                data = user.strip().split(",")
                with open("Stocks.txt", "r+") as f2:
                    stock_name = input("Enter name of stock to sell: ")
                    stocks = f2.readlines()
                    found = False
                    for stock in stocks:
                        if stock_name in stock:
                            found = True
                            print(stock)
                            stock_data = stock.strip().split(",")
                            stock_data[1] = str(int(stock_data[1]) + 1)
                            stocks.remove(stock)
                            stocks.insert(0, ",".join(stock_data) + "\n")
                            data[3] = str(int(data[3]) + int(stock_data[2]))
                            data[4] = str(int(data[4]) - 1)
                            users.remove(user)
                            users.insert(0, ",".join(data) + "\n")
                    if not found:
                        print("Stock not found")
                        exit()
                    f2.seek(0)
                    f2.truncate()
                    for stock in stocks:
                        f2.write(stock)
                f1.seek(0)
                f1.truncate()
                for user in users:
                    f1.write(user)


def display_user(name):
    with open("Users.txt", "r") as fobj:
        for user in fobj:
            if name in user:
                data = user.strip().split(",")
                print("Name: {}\nStock Quantity: {}\nMoney: {}\n".format(data[2], data[4], data[3]))


def Display():
    with open("Stocks.txt", "r") as fobj:

        for i in fobj:
            j = i.strip().split(",")
            if j:
                name = j[0]
                quant = j[1]
                price = j[2]

            print("Stock Name : {}  Stock Quantity : {}  Stock Price : {}".format(name, quant, price))


def Login():
    username = input("Enter your User Name : ")
    password = input("Enter your password : ")
    with open("Users.txt", "r") as fobj:
        for i in fobj:
            j = i.strip().split(",")
            st_user, st_pass = j[:2]
            if username == st_user and password == st_pass:
                print("Login Successfull !")
                while True:
                    print("1. Display my profile ")
                    print("2. Buy Stock ")
                    print("3. Sell Stock ")
                    print("4. Logout ")
                    ch = int(input("Enter your choice : "))
                    if ch == 1:
                        display_user(username)
                    elif ch == 2:
                        Buy(username)
                    elif ch == 3:
                        Sell(username)
                    elif ch == 4:
                        print("Logging out.....")
                        return
                    else:
                        print("Invalid Input !")
                        return
                else:
                        print("Invalid Username ! ")


def Register():
    username = input("Enter a new username: ")
    password = input("Enter a new password: ")
    name = input("Enter your name: ")
    money = input("Enter your starting money amount: ")

    with open("Users.txt", "a") as file:
        file.write("{},{},{},{},0\n".format(username,password,name,money))

    print("Registration successful!")       


while True:
    print("1.Display Stocks")
    print("2.Login Existing User")
    print("3.Register new User")
    print("4.Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        Display()
    elif ch == 2:
        Login()
    elif ch == 3:
        Register()
    elif ch == 4:
        break
    else:
        print("Invalid Option !")
