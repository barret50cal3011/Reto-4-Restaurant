from PaymentMethods.PaymentMethod import PaymentMethod as PM

class Cash(PM):

    def __init__(self, i_amount) -> None:
        super().__init__(i_amount)

    
    def pay(self, i_amount):
        if(self._check.calc_amount() < i_amount):
            self._log_payment(i_amount);
        else:
            raise Exception("i_amount not enough to pay the check")

    def _log_payment(self, i_amount):
        file = open(self._file_str, "a")
        file.write(f"Client payed {i_amount} in cash, change: { i_amount - self._check.calc_amount() }, check value = {self._check.calc_amount()}\n")
        file.close()