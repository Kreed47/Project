


def Display():
    with open("Stocks.txt","r") as fobj:
       
        
        for i in fobj:
            j=i.strip().split(',')
            if j:
                name = j[0]
                quant = j[1]
                price = j[2]
            
            print("Stock Name : {}  Stock Quantity : {}  Stock Price : {}".format(name,quant,price))
        




while (True):
    print("1.Display Stocks: ")
    print("2.Login Existing User : ")
    print("3.Register new User : ")
    print("4.Exit")
    ch=int(input("Enter your choice : "))
    if ch==1:
        Display()
    elif ch==2:
        Login():
    elif ch==3:
        Register():
    elif ch==4:
        break
    else :
        print("Invalid Option !")
        



def Login():
    username = input("Enter your User Name : ")
    password = input("Enter your password : ")
    with open("Users.txt","r") as fobj:
        for i in fobj:
            j=i.strip().split(',')
            st_user, st_pass = j[:2]
            if (username == st_user and password == st_pass):
                print("Login Successfull !")
                while (True):
                    print("1.Display my profile : ")
                    print("2. Buy Stock ")
                    print("3. Sell Stock ")
                    print("4. Logout ")
                    choice = int(input("Enter your choice : "))
                    if ch==1:
                        display_user(username):
                    elif(ch==2):
                        Buy(username)
                    elif(ch==3):
                        Sell(username)
                    elif (ch==4):
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
        file.write(f"{username},{password},{name},{money},0\n")
    
    print("Registration successful!")

