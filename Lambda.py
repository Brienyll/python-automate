#named function
def notLam(x):
    return x+2 + 5*x + 4
print(notLam(-4))

#lambda
print((lambda x: x+2 + 5*x + 4) (-4))
