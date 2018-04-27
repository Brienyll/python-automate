from itertools import accumulate, takewhile

nums = list(accumulate(range(8)))
print(nums)
print(list(takewhile(lambda x: x<= 6, nums)))

# [0, 1, 3, 6, 10, 15, 21, 28] # 0+1, 1+2, 3+3, 6+4, 10 + 5, 15 + 6, 21 + 8
# [0, 1, 3, 6] # 0+1, 1+2, 3+3
