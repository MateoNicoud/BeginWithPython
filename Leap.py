def leapYears(i):
    if i % 400 == 0:
        return "leap"
    elif i % 100 == 0 and i % 400 != 0:
        return "normal"
    elif i % 4 ==0 and i % 100 != 0:
        return "leap"
    elif i % 4 !=0:
        return "normal"
    else:
        return "error"



print(leapYears(2013))