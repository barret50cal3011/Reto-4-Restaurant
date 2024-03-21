class MenuItem:

    def __init__(self, i_name, i_price) -> None:
        self._name = i_name
        self._price = i_price

    @property
    def price(self):
        return self._price
    
    @property
    def name(self):
        return self._name