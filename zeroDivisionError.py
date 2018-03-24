a = input('input a number ')
b = input('type another number ')
a = int(a)
b = int(b)
try:
    print(a/b)
except ZeroDivisionError:
    print('b cannet be zero. Try again')  

def add(x,y):
    """
Returns x+y.
    :param x:int first integer to be added.
    :param :int second integer to be added.
    :return: int sum of x and y.
    """
    return x + y

print(add(2,9))
