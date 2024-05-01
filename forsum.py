numbers=input("enter numbers you want to enter")
list=numbers.split()
count=0
for i in list:
    count=count+1
for i in range(count):
    list[i]=int(list[i])
sum=0
for i in range(count):
    sum=sum+list[i]
avg=sum/count
print(list)
print( "sum is",sum)
print("average is ",round(avg))



