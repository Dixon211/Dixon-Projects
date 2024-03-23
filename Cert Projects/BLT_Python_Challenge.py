import os

dir = r"C:\Users\Assoc\Downloads\Resources\Python_Challenge\L0_D1"

contents = os.listdir(dir)

for item in contents:
    print("\n" + item)
print("\n")