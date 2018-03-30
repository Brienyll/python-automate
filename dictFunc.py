pairs = {1: "apple",
    "orange": [2, 3, 4], 
    True: False, 
    None: "True",
}

print(pairs.get("orange"))
print(pairs.get(7))
print(pairs.get(False, "not in dictionary"))
