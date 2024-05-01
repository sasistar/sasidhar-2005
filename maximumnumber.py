number=input("enter numbers")
list=number.split()
count=0
for i in list:
    count=count+1
for i in range(count):
    list[i]=int(list[i])
maximum_element=list[0]
for i in range(count):
    if list[i]>maximum_element:
        number=list[i]
print("maximum number is", number)