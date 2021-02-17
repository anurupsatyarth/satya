#this is the the parent class used as blueprint


class MenuItem:
    food_menu = { "r1": {"f1": 24,"f2": 40, "f3":54, "f4":56} ,
                  "r2": {"f1": 24, "f2": 40, "f3": 54, "f4": 56}
                 }

    def __init__(self):
        pass

    def disp_menu(self, id):
        if id in self.food_menu.keys():
            print(self.food_menu.get(id))

    def add_item(self, id, menu):
        if id not in self.food_menu.keys():
            self.food_menu[id] = menu

    def update_item(self, id,item_name, item_price):
        if id not in self.food_menu.keys():
            print("food name is not present in the Menu")
        else:
            self.food_menu[id][item_name]= item_price

    def del_item(self, userid, item_name):
        self.food_menu[userid].pop(item_name)


    def get_total_price(self, count):
        total_price = self.price * count
        return round(total_price)