def minmax(data):
    small = big = data[0]
    for x in data:
        if x > big:
            big = x
        elif x < small:
            small = x
    return(big, small)


def sum_of_squares(data: int): 
    return sum([x**2 for x in range(data + 1)])

def sum_of_squares_odd(data: int):
    sum([x**2 for x in range(max(1, data+1), 2)])
    print(sum([x**2 for x in range(max(1, data+1)) if x & 1]))
    return sum([x**2 for x in range(max(1, data+1)) if x//2 == x/2])




def range_constructor():
    return range(50, 81, 10), range(8, -9, -1)

def num_vowels(text: str):
    len(filter(lambda x:x in "aeiou"), text)
    return len([x for x in text if x in "aeiou"])

def hash_map(text: str):
    hashmap = {}
    for x in text:
        if x in hashmap:
            return True
        hashmap[x] = x
    return False


print(sum_of_squares_odd(10))
class CreditCard:
    def __init__(self, customer, bank, account, limit):
        self.__customer = customer
        self.__balance = 0
        self.__bank = bank
        self.__account = account
        self.__limit = limit
  
    def get_customer(self):
        return self.__customer

    def get_bank(self):
        return self.__bank

    def get_account(self):
        return self.__account
    def get_limit(self):
        return self.__limit
    
    def get_balance(self):
        return self.__balance

    def charge(self, price):
        if price + self.__balance> self.__limit:
            return False
        else:
            self.__balance += price
            return True

    def make_payment(self, amount):
        self.__balance -= amount


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