from dsa import CreditCard

class PredatoryCreditCard(CreditCard):
    def __init__(self, customer, bank, account, limit, apr):
        super().__init__(customer, bank, account, limit)
        self.__apr = apr
        self.__charge_no = 0
      
    

    def charge(self, price):
        self.__charge_no += 1
        if price + self.get_balance() > self.get_limit():
            self.make_payment(5)
            return False
        else:
            self.make_payment(-5)
            return True

    def process_month(self):
        return (1- ((self.__apr + 1)**(1/12)))  + max(0, self.__charge_no - 10) * 1

if __name__ == "__main__":
    wallet = []
    wallet.append(CreditCard("John Lee", "DBS", "2032839232", 2500))
    wallet.append(CreditCard('John Lee', 'OCBC',
    '3485 0399 3395 1954', 3500) )
    wallet.append(CreditCard('John Lee', 'Maybank',
    '5391 0375 9387 5309', 5000) )
    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(2 * val)
        wallet[2].charge(3 * val)
    
    for c in range(3):
        print("Customer =", wallet[c].get_customer())
        print("Bank = ", wallet[c].get_bank())
        print("Account = ", wallet[c].get_account())
        print("Limit = ", wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print("new balance =", wallet[c].get_balance())
        print()