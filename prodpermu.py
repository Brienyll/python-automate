from itertools import product, permutations

letters = ("A", "Z")
print(list(product(letters, range(2))))
print(list(permutations(letters))) 

# A 0, A 1, Z 0, Z 1
# A Z, Z A
