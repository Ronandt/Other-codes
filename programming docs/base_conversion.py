while 1:
    try:
        y = float(input("What Number (Press any character to quit): "))
        #u = int(input("What base do you want to convert from?"))
        v = int(input("What base (Up to 16) do you want to convert to: "))
    except ValueError:
        print("Quit!")
        break

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
        for l in range(10):
            p.append(str(int(b // 1)))
            b = b % 1 * v
        if v <= 10:
            k += "".join(p) + "."
        elif 10 < v <= 16:
            k += "".join([dict[x] if int(x) >= 10 else x for x in p]) + "."
        else:
            pass
    while y != 0:
        f.append(str(int(y % v)))
        y //= v
    if v <= 10:
        k += "".join(f)[::-1]
    elif 10 < v <=16:
        k += "".join([dict[x] if int(x) >= 10 else x for x in f][::-1])
    else:
        print("Invalid Input!")
    print(k)