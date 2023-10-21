def careless_div(a, b):
    try:
        s = a/b
    except ZeroDivisionError:
        if a>0:
            s = float('+inf')
        elif a<0:
            s = float('-inf')
        else:
            s = -17.5
    return s
print(careless_div(2, 2))
print(careless_div(-2, 0))
print(careless_div(0, 0)) 
