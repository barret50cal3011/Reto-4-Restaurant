from MenuItems.MenuItem import MenuItem

class Beverage(MenuItem):

    def __init__(self, i_name, i_price):
        super().__init__(i_name, i_price)