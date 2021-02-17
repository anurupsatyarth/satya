from pip._vendor.distlib.compat import raw_input

from authenticate import Authentication
from resturants import restaurantName
from users import userName
from menuitem import MenuItem

def order():
    name = str(input(" Select the restaurant : "))
    r = restaurantName()
    r.restSearch(name)
    n = int(input(""))
    print("Enter food item to be ordered in the given format: 'Food name : food quantity ")
    menu = dict(raw_input().split(":") for _ in range(n))




def prof_func(id ):
    user_menu = 0
    while user_menu !=1:

        print("Choose the options below.")
        print("1. Create/update profile")
        print("2. Browse restaurants and place orders")
        print("3. Exit")
        choice = int(input())
        if choice == 1:
            profile_m= True
            while profile_m == True:


                print("Choose the options below.")
                print("1. Create your profile")
                print("2. Update your profile")
                print("3. Delete your profile")
                print("4. Display your profile")
                print("6. Exit")
                user_input = int(input())
                if user_input == 1:

                    print("enter you data: ")
                    name = str(input("enter your name: "))
                    age = int(input("enter your age: "))
                    gender = str(input("enter your gender: "))
                    phone_num = str(input("enter your number: "))
                    profile = [name, age, gender, phone_num]
                    u = userName()
                    u.CreateProfile(id, profile)
                    u.displayprofile(id)

                elif user_input == 2:
                    print("Enter values to update")
                    name = str(input("enter your name: "))
                    age = int(input("enter your age: "))
                    gender = str(input("enter your gender: "))
                    phone_num = str(input("enter your number: "))
                    profile = [name, age, gender, phone_num]
                    u = userName()
                    u.UpdateProfile(id, profile)
                    u.displayprofile(id)

                elif user_input == 3:
                    u = userName()
                    u.deleteProfile(id)
                    profile_m =False

                elif user_input == 4:
                    u = userName()
                    u.displayprofile(id)

                elif user_input == 5:pass

                else:
                    profile_m = False
        elif choice == 2:
            rest_order = True
            while rest_order == True:
                print("choose the below options")
                print("1. Browse the restaurants.")
                print("2. Search a restaurant.")
                print("3. Exit.")
                user_choice = int(input())

                if user_choice == 1:
                    r = restaurantName()
                    for i in (r.restBrowse()):
                        print(i)
                    order()


                elif user_choice == 2:
                    rest_name = str(input("enter the restaurant name to be searched:"))
                    r = restaurantName()
                    r.restSearch(rest_name)
                else:
                    rest_order = False

        else:
            user_menu = 1


def main():
    exit= ''
    while exit!= 'exit' :
        print("------------------------------------------------")
        print("1. Register as a User")
        print("2. Register as a restaurant")
        print("3. to exit")
        user_kind = input("Type 1 or 2 so select from above")
        print("------------------------------------------------")

        if int(user_kind) == 1:  # for user
            print("1. New User")
            print("2. Existing User")
            argument = int(input("Are you a new user or existing user, choose 1 or 2?"))
            print("------------------------------------------------")

            if argument == 1:   # signup and login
                id = input("Enter unique user id: ")
                #name = input("Enter your name: ")
                password = input("Enter your password: ")
                new_user = userName()
                new_user.userSignUp(id, password)
                print("please login")
                id = input("Enter unique user id: ")
                # name = input("Enter your name: ")
                password = input("Enter your password: ")
                login_stat = userName()
                login_stat.userLogin(id, password)
                prof_func(id)
            else:   # only login
                id = input("Enter your userid: ")
                password = input("Enter your password: ")
                login_stat = userName()
                login_stat.userLogin(id, password)
                prof_func(id)
        elif int(user_kind)==2 :  # FOR RESTAURANT
            print("1. New Restaurant")
            print("2. Existing Restaurant")
            argument = int(input("Are you a new user or existing user, choose 1 or 2?"))
            print("------------------------------------------------")
            if argument == 1:
                id = input("Enter unique user id: ")
                #name = input("Enter your name: ")
                password = input("Enter your password: ")
                new_user = restaurantName()
                new_user.restSignUp(id, password)
                print("please login")
                id = input("Enter unique user id: ")
                # name = input("Enter your name: ")
                password = input("Enter your password: ")
                login_stat = restaurantName()
                login_stat.restLogin(id, password)
            else:
                id = input("Enter your userid: ")
                password= input("Enter your password: ")
                login_stat= restaurantName()
                login_stat.restLogin(id, password)
                menu_exit= 0
                while menu_exit!= 1:
                    print("Choose the options below.")
                    print("1. Create/Add Menu items")
                    print("2. Update Menu Items")
                    print("3. Delete Menu Items")
                    print("4. Display Menu Items")
                    print("5. Exit")
                    c_menu = int(input())
                    if c_menu == 1 :

                        print("Enter one item at a time in the given format: 'Food name : food price ")
                        n= int(input("Enter the number of items you want to add: "))
                        menu = dict(raw_input().split(":") for _ in range(n))
                        m = MenuItem()
                        m.add_item(id, menu)
                        m.disp_menu(id)

                    elif c_menu == 2:
                        print("Enter the item name for which price has to be updated :")
                        item_name = str(input())
                        print("Enter the updated price of the item:")
                        item_price= int(input())
                        m = MenuItem()
                        m.update_item(id, item_name, item_price)
                        m.disp_menu(id)

                    elif c_menu == 3:
                        item_name =str(input("Enter the name of item which has to be deleted: "))
                        m = MenuItem()
                        m.del_item(id, item_name)
                        m.disp_menu(id)

                    elif c_menu == 4:
                        m = MenuItem()
                        m.disp_menu(id)

                    else:
                        menu_exit = 1
        else:
            exit='exit'







if __name__ == "__main__":
    main()