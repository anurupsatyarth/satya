# Import the MenuItem class using 'from' 'import'

from menuitem import MenuItem

# Inherit the MenuItem class and define the Drink class
# here we have overide the info and init funct of menu_item
class Drink(MenuItem):
    def __init__(self, name, price, volume):
         # Using super() call __init__() from the parent class
        super().__init__(name, price)
        self.volume = volume

    def info(self):
        return (self.name + ': $' + str(self.price) + ' (' + str(self.volume) + 'mL)')