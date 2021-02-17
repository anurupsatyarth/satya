from resturants import restaurantName
from users import userName


class Authentication():
    def __init__(self, argument,user_kind):
        if user_kind =='U':
            if argument == 1:  # new user
                new_user = userName.userSignUp()  #signup for users
                if new_user== True:
                    print("Registration successful !!")
                else:
                    print("User already Exists..")

                login_stat = userName.userLogin()   # login for users
                if login_stat== True:
                    print("Login  successful !!")
                else:
                    print("Invalid username/password. Try again.")

            else:                # existing user
                login_stat = userName.userLogin()  # login for users
                if login_stat == True:
                    print("Login  successful !!")
                else:
                    print("Invalid username/password. Try again.")
        else:
            if argument == 1:  # new restaurant
                new_user = restaurantName.restSignUp()  # signup for restaurant
                if new_user == True:
                    print("Registration successful !!")
                else:
                    print("User already Exists..")

                login_stat = restaurantName.restLogin()  # login for restaurant
                if login_stat == True:
                    print("Login  successful !!")
                else:
                    print("Invalid username/password. Try again.")

            else:  # existing user
                login_stat = restaurantName.restLogin()  # login for restaurant
                if login_stat == True:
                    print("Login  successful !!")
                else:
                    print("Invalid username/password. Try again.")






