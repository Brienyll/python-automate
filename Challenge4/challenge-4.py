"""
Write a program with two functions. The first function should take an integer
divided by two. The second finction should take an integer as a parameter and
return the result as a variable, and pass it as a parameter to the second
function
"""

def divideByTwo(n):
    return n / 2
def multiplyByFour(n):
    return n * 4

y = divideByTwo(4)
x = multiplyByFour(y)

print(x)
