# Import the MenuItem class using 'from' 'import'


from menuitem import MenuItem


# Inherit the MenuItem class and define the Food class
# here we have overide the info and init funct of menu_item
class Food(MenuItem):
    def __init__(self, name, price, calorie_count):
        # Using super() call __init__() from the parent class
        super().__init__(name, price)
        self.calorie_count = calorie_count

    def info(self):
        return self.name + ': $' + str(self.price) + ' (' + str(self.calorie_count) + 'kcal)'

    def calorie_info(self):
        print('kcal: ' + str(self.calorie_count))