"""
Writ a function that converts a string to a float and returns the result.
Use exception handling to catch the exception that could occur.
"""
def stringToFloat(s):
    try:
        return float(s)
    except(ValueError):
        print("Invalid Input")
sf = stringToFloat("67")
print(sf)
