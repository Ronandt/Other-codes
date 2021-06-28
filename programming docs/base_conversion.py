import sys
def hexConverter():
    while 1:
        try:
            y = float(input("What Number (Press any character to quit): "))
            v = int(input("What base (Up to 16) do you want to convert to: "))
            z = int(input("What is the precision you want to set it to: "))
            if z < 0:
                print("Precision cannot be negative!")
                sys.exit()
        except ValueError:
            print("Quit!")
            break
        n, f, p, k = '0', [], [], ""
        dict = {
            "10" : "A",
            "11" : "B",
            "12": "C",
            "13": "D",
            "14": "E",
            "15": "F",
        }
        c = abs(y)
        if c % 1 != 0:
            b = c % 1 * v
            c -= c % 1
            for l in range(z):
                p.append(str(int(b // 1)))
                b = b % 1 * v
            if v <= 10:
                n = "".join(p)
            elif 10 < v <= 16:
                n = "".join([dict[x] if int(x) >= 10 else x for x in p])
            else:
                pass
        while y != 0:
            f.append(str(int(y % v)))
            c //= v
        if v <= 10:
            o = "".join(f)[::-1]
        elif 10 < v <=16:
            o = "".join([dict[x] if int(x) >= 10 else x for x in f][::-1])
        else:
            print("Invalid Input!")
            sys.exit()

        print((y < 0) * "-" + o + "." + n)



print(hexConverter())
