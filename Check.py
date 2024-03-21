from MenuItems.MenuItem import MenuItem
class Check:

    def __init__(self):
        self.__items = {}
        self.__discount_percent = []
        self.__discount_value = []

    
    def add_item(self, i_item: MenuItem, i_amount:int = 1):
        if(self.__items[i_item.name] == None):
            self.__items[i_item.name] = i_amount
        else:
            self.__items[i_item.name] += i_amount

    
    def apply_dicount_percent(self, i_discount):
        self.__discount_percent.append(i_discount)

    def apply_discount_value(self, i_discount):
        self.__discount_value.append(i_discount)

    def calc_amount(self):
        amount = 0
        for item in self.__items:
            amount += self.__items[item].price
        
        discount = 0
        for value in self.__discount_value:
            #max discount value
            if (discount + value) / amount > 0.2:
                amount *= 0.8
                discount = 0
                break
            else:
                discount += value
        
        amount -= discount

        for percent in self.__discount_percent:
            amount *= (1 - percent)

        #add IVA
        amount *= 1.21
        return amount