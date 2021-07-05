import time
import random
passLenght = int(input("Enter the length of password:  "))
print("Generating Password...")
# time.sleep(2)
password = ""
string = "adlbafdoqieruwonxcnvxcnd928375&sdfajsfljalsfdjsalfjln,mnncxvhSDF&(^&#$!!#$^$%^%^%^dff544"
while len(password) != passLenght:
    character = random.randint(0,len(string))
    password = password+string[character]
print(password)



