import sys
while 1:
    try:
        y = float(input("What Number (Press any character to quit): "))
        #u = int(input("What base do you want to convert from?"))
        v = int(input("What base (Up to 16) do you want to convert to: "))
        z = int(input("What is the precision you want to set it to: "))
        if z < 0:
            print("Precision cannot be negative!")
            sys.exit()
    except ValueError:
        print("Quit!")
        break
    n = '0'
    f = []
    p = []
    k = ""
    dict = {
        "10" : "A",
        "11" : "B",
        "12": "C",
        "13": "D",
        "14": "E",
        "15": "F",
    }
    if y % 1 != 0:
        b = y % 1 * v
        y -= y % 1
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
        y //= v
    if v <= 10:
        o = "".join(f)[::-1]
    elif 10 < v <=16:
        o = "".join([dict[x] if int(x) >= 10 else x for x in f][::-1])
    else:
        print("Invalid Input!")
        sys.exit()

    print(o + "." +  n)
