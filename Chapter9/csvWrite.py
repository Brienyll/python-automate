import csv
import os

os.chdir(r'\Users\student\Desktop\pythonautomate')

with open("st.csv", "w", newline='') as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(['one',
                'two',
                'three'])
    w.writerow(['four',
                'five',
                'six'])
    
