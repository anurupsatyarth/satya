from menuitem import MenuItem
class restaurantName:
    rest_name = {"r1":'r1@123'}

    def __init__(self):
        pass

    def restSignUp(self, userid, password):
        if userid not in self.rest_name.keys():
            self.rest_name[userid] = password
            print("Registration successful !!")
        else:
            print("User already Exists..")

    def restLogin(self, userid, password):

        if (userid in self.rest_name.keys()) and (str(self.rest_name.get(userid)) == password):
            print("Login  successful !!")
        else:
            print("Invalid username/password. Try again.")

    def restBrowse(self):
        key = self.rest_name.keys()
        return key


    def restSearch(self, r_name):
        key = self.rest_name.keys()
        if r_name in key:
            print(r_name, MenuItem.food_menu.get(r_name))
        else:
            print("restaurant not found")

    def deluser(self, userid):
        rest_name.remove(userid)

    def displayusers(self):
        return self.rest_name
