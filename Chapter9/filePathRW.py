import os

print(os.getcwd())

os.chdir('/Users/standart/Desktop/Brix Files/Projects/python')

print(os.getcwd())

op = open("test.txt", "w")
op.write("Hello there!")
op.close()


with open("test.txt", "r") as f:
    print(f.read())

