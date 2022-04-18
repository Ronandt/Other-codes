from dsa import CreditCard

class PredatoryCreditCard(CreditCard):
    def __init__(self, customer, bank, account, limit, apr):
        super().__init__(customer, bank, account, limit)
        self.__apr = apr
      
    

    def charge(self, price):
        if price + self.get_balance() > self.get_limit():
            self.__balance -= 5
            return False
        else:
            self.__balance += price
            return True

    def process_month(self):
        return (1- ((self.__apr + 1)**(1/12))) * self.__balance

objects = PredatoryCreditCard("DFDS","DBS", "438 238 193 391", 2500, 1.2944 )

objects.charge(2499)
objects.process_month()