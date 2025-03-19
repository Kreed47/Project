with open("stocks2.txt", "a") as stock_file:
    pass
class Stocks:
    def __init__(self, filename):
        self.filename = filename

    def display_stocks(self):
        with open(self.filename, "r") as stock_file:
            for line in stock_file:
                stock_data = line.strip().split(",")
                print("Stock Name: {}  Stock Quantity: {}  Stock Price: {}".format(stock_data[0], stock_data[1], stock_data[2]))

    def buy_stock(self, stock_name, quantity):
        with open(self.filename, "r+") as stock_file:
            stocks = stock_file.readlines()
            for i, stock in enumerate(stocks):
                if stock_name in stock:
                    stock_data = stock.strip().split(",")
                    if int(stock_data[1]) < quantity:
                        print("Insufficient stock quantity")
                        return False
                    stock_data[1] = str(int(stock_data[1]) - quantity)
                    stocks[i] = ",".join(stock_data) + "\n"
                    stock_file.seek(0)
                    stock_file.truncate()
                    stock_file.writelines(stocks)
                    print("Stock purchased successfully.")
                    return True
            print("Stock not found")
            return False

    def sell_stock(self, stock_name, quantity):
        with open(self.filename, "r+") as stock_file:
            stocks = stock_file.readlines()
            for i, stock in enumerate(stocks):
                if stock_name in stock:
                    stock_data = stock.strip().split(",")
                    stock_data[1] = str(int(stock_data[1]) + quantity)
                    stocks[i] = ",".join(stock_data) + "\n"
                    stock_file.seek(0)
                    stock_file.truncate()
                    stock_file.writelines(stocks)
                    print("Stock sold successfully.")
                    return True
            print("Stock not found")
            return False


class Users:
    def __init__(self, filename):
        self.filename = filename

    def display_user_profile(self, user_name):
        with open(self.filename, "r") as user_file:
            for user in user_file:
                data = user.strip().split(",")
                if user_name == data[0]:
                    print("Name: {}\nStock Quantity: {}\nMoney: {}\n".format(data[2], data[4], data[3]))
                    return
            print("User not found")

    def buy_stock(self, user_name, stock_name, quantity, price):
        with open(self.filename, "r+") as user_file:
            users = user_file.readlines()
            for i, user in enumerate(users):
                data = user.strip().split(",")
                if user_name == data[0]:
                    if int(data[3]) < quantity * price:
                        print("Insufficient funds")
                        return False
                    data[3] = str(int(data[3]) - quantity * price)
                    data[4] = str(int(data[4]) + quantity)
                    users[i] = ",".join(data) + "\n"
                    user_file.seek(0)
                    user_file.truncate()
                    user_file.writelines(users)
                    print("Stock purchased successfully.")
                    return True
            print("User not found")
            return False

    def sell_stock(self, user_name, stock_name, quantity, price):
        with open(self.filename, "r+") as user_file:
            users = user_file.readlines()
            for i, user in enumerate(users):
                data = user.strip().split(",")
                if user_name == data[0]:
                    if int(data[4]) < quantity:
                        print("Insufficient stock quantity")
                        return False
                    data[3] = str(int(data[3]) + quantity * price)
                    data[4] = str(int(data[4]) - quantity)
                    users[i] = ",".join(data) + "\n"
                    user_file.seek(0)
                    user_file.truncate()
                    user_file.writelines(users)
                    print("Stock sold successfully.")
                    return True
            print("User not found")
            return False


if __name__ == "__main__":
    stocks_manager = Stocks("stocks2.txt")
    users_manager = Users("users2.txt")

    while True:
        print("1. Display Stocks")
        print("2. Login Existing User")
        print("3. Register New User")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            stocks_manager.display_stocks()
        elif choice == "2":
            username = input("Enter your User Name: ")
            password = input("Enter your password: ")
            # Check login credentials here
            while True:
                print("1. Display my profile")
                print("2. Buy Stock")
                print("3. Sell Stock")
                print("4. Logout")
                user_choice = input("Enter your choice: ")
                if user_choice == "1":
                    users_manager.display_user_profile(username)
                elif user_choice == "2":
                    stock_name = input("Enter name of stock to purchase: ")
                    quantity = int(input("Enter quantity to purchase: "))
                    price = int(input("Enter price per unit: "))  # Assuming price is provided
                    stocks_manager.buy_stock(stock_name, quantity)
                elif user_choice == "3":
                    stock_name = input("Enter name of stock to sell: ")
                    quantity = int(input("Enter quantity to sell: "))
                    price = int(input("Enter price per unit: "))  # Assuming price is provided
                    stocks_manager.sell_stock(stock_name, quantity)
                elif user_choice == "4":
                    print("Logging out...")
                    break
                else:
                    print("Invalid Input!")
        elif choice == "3":
            # Implement user registration
            pass
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid Option!")
