import os

my_list = list()

with open("test.txt", "r") as f:
    my_list.append(f.read())

print(my_list)
