import csv
import os

os.chdir(r'\Users\student\Desktop\pythonautomate')

with open("st.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))
