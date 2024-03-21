from PaymentMethods.PaymentMethod import PaymentMethod as PM
from Check import Check

class Card(PM):

    def __init__(self, number, cvv, i_check: Check) -> None:
        super().__init__(i_check)
        self.__number = number
        self.__cvv = cvv

    def pay(self):
        if(not self.__card_transaction_passed()):
            raise Exception("transaction was declined by bank")
        else:
            self._log_payment()
            super().pay()

    def _log_payment(self):
        file = open(self._file_str, "a")
        file.write(f"Client payed with Card ending in {str(self.__number)[-4:]} check value = {self._check.calc_amount()}\n")
        file.close()

    #method created to simulate card passing or declinig
    def __card_transaction_passed(self):
        return len(str(self.__cvv)) == 3 and len(str(self.__number)) == 16