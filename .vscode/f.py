

'''class Iterable:
    def __init__(self, limit = 0):
        self._limit = limit

    @property
    def limit(self):
        return self._limit

    @limit.setter
    def limit(self, limit):
        self._limit = limit
    
    @limit.getter
    def limit(self):
        return f"Your limit is {self._limit}"
    
    def __iter__(self):
        self.current = 0
        return self
    
    def __next__(self):
        if self.current > self._limit:
            raise StopIteration
        self.current += 1
        return self.current
    

iterable = iter(Iterable())
print(next(iterable))
#The difference between a list comprehension and a generator is that geneartor only prints one by one, without storing in memory, while list comprehensions stores elements in a list 
#Iterators uses a class-based syntax to customise, however yield and geenartors are usually the way to go as there is no need for such a complex method for most cases
#Generators has lazy evaluation, only producing items when called with a for loop  when called
#The difference between just printing and yielding is that the printing function is called and printed upon getting calledl, while the generator function stores them.


def generator(start, stop):
    for x in range(start, stop):
        yield x * x
def print_generator(start, stop):
    for x in range(start, stop):
        print(x*x)

one = generator(1,5)
two = print_generator(1, 5)
for x in one:
    print(x)'''


def minmax(data: list):
    small = big = data[0]
    for x in data:
        if x < small:
            small = x
        elif x > big:
            big = x
    return (small, big)


print(minmax([3, 2, 2, 4]))


def sum_of_squares(n):
    return sum([x**2 for x in range(n + 1)])


print(sum_of_squares(10))


def sum_of_squares_odd(n):
    return sum([x ** 2 for x in range(1, n+1, 2)])


print(sum_of_squares_odd(10))


def range_constructor():
    range(50, 10, 81)
    range(8, -9, -1)


def num_vowels(text: str):
    len(list(filter(lambda x: x in "aeiou", text)))  # optional
    return len([x for x in text if x in "aeiou"])


def distinct(args):
    hash_map = {}
    for x in args:
        if x in hash_map:
            return False
        hash_map[x] = x
    return True

    # return len({x for x in args}) == len(args)
print(distinct([1, 2]))
