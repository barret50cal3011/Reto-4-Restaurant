from PaymentMethods.PaymentMethod import PaymentMethod as PM
from Check import Check

class Cash(PM):

    def __init__(self, i_check: Check) -> None:
        super().__init__(i_check)

    
    def pay(self, i_amount=0):
        if(self._check.calc_amount() < i_amount):
            self._log_payment(i_amount);
            del self._check
        else:
            raise Exception("i_amount not enough to pay the check")

    def _log_payment(self, i_amount):
        file = open(self._file_str, "a")
        file.write(f"Client payed {i_amount} in cash, change: { i_amount - self._check.calc_amount() },\
 check value = {self._check.calc_amount()}\n")
        file.close()