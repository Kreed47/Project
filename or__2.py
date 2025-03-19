class Stock:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def buy(self, quantity):
        if self.quantity < quantity:
            print("Insufficient stock quantity")
            return False
        self.quantity -= quantity
        return True

    def sell(self, quantity):
        self.quantity += quantity

    def display(self):
        print("Stock Name: {}  Stock Quantity: {}  Stock Price: {}".format(self.name, self.quantity, self.price))


class User:
    def __init__(self, username, password, name, money):
        self.username = username
        self.password = password
        self.name = name
        self.money = int(money)
        self.stocks = {}

    def buy_stock(self, stock, quantity):
        total_cost = stock.price * quantity
        if self.money < total_cost:
            print("Insufficient funds")
            return False
        if stock.buy(quantity):
            self.money -= total_cost
            if stock.name in self.stocks:
                self.stocks[stock.name] += quantity
            else:
                self.stocks[stock.name] = quantity
            return True
        return False

    def sell_stock(self, stock, quantity):
        if stock.name not in self.stocks or self.stocks[stock.name] < quantity:
            print("Insufficient stock quantity or stock does not exist.")
            return False
        stock.sell(quantity)
        self.money += stock.price * quantity
        self.stocks[stock.name] -= quantity
        return True

    def display_profile(self):
        print("Name: {}\nMoney: {}\nStocks: {}".format(self.name, self.money, self.stocks))


def load_stocks_from_file(filename):
    stocks = []
    try :
        with open(filename, "r") as f:
            for line in f:
                name, quantity, price = line.strip().split(",")
                stocks.append(Stock(name, int(quantity), int(price)))
    except FileNotFoundError:
        print("Stocks File not found !")
    return stocks


def load_users_from_file(filename):
    users = {}
    try: 
        with open(filename, "r") as f:
            for line in f:
                username, password, name, money, _ = line.strip().split(",")
                users[username] = User(username, password, name, int(money))
    except FileNotFoundError:
        print("Users File not found !")
    return users


def save_users_to_file(filename, users):
    try:
        with open(filename, "w") as f:
            for user in users.values():
                stocks_info = ",".join(["{},{}".format(stock, quantity) for stock, quantity in user.stocks.items()])
                f.write("{},{},{},{},{}\n".format(user.username, user.password, user.name, user.money, stocks_info))
    except Exception as e:
        print("Error occured while saving users in file :",e)



def main():
    stocks = load_stocks_from_file("Stocks.txt")
    users = load_users_from_file("Users.txt")

    while True:
        print("1. Display Stocks")
        print("2. Login Existing User")
        print("3. Register New User")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            for stock in stocks:
                stock.display()
        elif choice == "2":
            username = input("Enter your User Name: ")
            password = input("Enter your password: ")
            if username in users and users[username].password == password:
                current_user = users[username]
                print("Login successful!")
                while True:
                    print("1. Display my profile")
                    print("2. Buy Stock")
                    print("3. Sell Stock")
                    print("4. Logout")
                    user_choice = input("Enter your choice: ")
                    if user_choice == "1":
                        current_user.display_profile()
                    elif user_choice == "2":
                        stock_name = input("Enter name of stock to purchase: ")
                        quantity = int(input("Enter quantity to purchase: "))
                        for stock in stocks:
                            if stock.name == stock_name:
                                if current_user.buy_stock(stock, quantity):
                                    print("Stock purchased successfully.")
                                break
                        else:
                            print("Stock not found")
                    elif user_choice == "3":
                        stock_name = input("Enter name of stock to sell: ")
                        quantity = int(input("Enter quantity to sell: "))
                        if stock_name in current_user.stocks:
                            for stock in stocks:
                                if stock.name == stock_name:
                                    if current_user.sell_stock(stock, quantity):
                                        print("Stock sold successfully.")
                                    break
                            else:
                                print("Stock not found")
                        else:
                            print("You do not own this stock")
                    elif user_choice == "4":
                        print("Logging out...")
                        break
                    else:
                        print("Invalid Input!")
            else:
                print("Invalid username or password")
        elif choice == "3":
            username = input("Enter a new username: ")
            if username in users:
                print("Username already exists!")
                continue
            password = input("Enter a new password: ")
            name = input("Enter your name: ")
            money = input("Enter your starting money amount: ")
            users[username] = User(username, password, name, money)
            print("Registration successful!")
        elif choice == "4":
            save_users_to_file("Users.txt", users)
            print("Exiting...")
            break
        else:
            print("Invalid Option!")


main()
