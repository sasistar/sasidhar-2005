import random
letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S']
numbers=['1','2','3','4','5','6','7','8','9']
char=['@','#','*','(']
a=int(input("how many letters you want to enter"))
b=int(input("how many numbers you want to enter"))
c=int(input("how many characters you want to enter"))
password=[]
for i in range(a):
    s=random.choice(letters)
    password.append(s)
for i in range(b):
    s=random.choice(numbers)
    password.append(s)
for i in range(c):
    s=random.choice(char)
    password.append(s)
random.shuffle(password)
passi=""
for i in password:
    passi=passi+i
print(passi)
print("sasi")


    
