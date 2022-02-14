test = 10000000
   
   
   
if len(str(test)) >= 4:
    print(f'${str(test)[:-3]},{str(test)[-3:]}')
else:
    print(f"${test}")