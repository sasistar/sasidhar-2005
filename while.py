# number=int(input("enter your number(-1 for exit)"))
# while number!=-1:
#     print(number)
#     number=int(input("enter your number(-1 for exit)"))


#sum of numbers
total=0
number=int(input("enter number(press 0 to terminate)"))
while number!=0:
    total= total+number
    number=int(input("enter number(press 0 to terminate)"))
print(f"total is{total}")
