s1={1,2,3,4,5,6}
s2={6,7,8,9,10}
s3={11}
#print(s1.union(s2))
#print(s1|s2)
#print(s1|s2|s3)
#print(s1.union(('sasi','ramesh','bulli')))
# s1.update(s2)
# print(s1)
# s1.update(['sasi','bulli'])
# print(s1)
# print(s1.intersection(s2))
# print(s1 & s2)
s1.intersection_update(s2)
print(s1)