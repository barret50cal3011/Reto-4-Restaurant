from Check import Check
class PaymentMethod:

    _file_str = "./docs/payments.log"

    def __init__(self, i_check: Check) -> None:
        self._check = i_check


    @property
    def amount(self):
        return self._amount

    def pay(self):
        del self._check
    
    def _log_payment(self):
        raise NotImplementedError("Method not implemented")