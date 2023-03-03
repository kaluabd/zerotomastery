# list unpacking
# assigning variable names for sequential objects in list

a,b,c = [1,2,3]

print(a)
print(b)
print(c)

a,b,c, *new, d = [1,2,3,4,5,6,7]

print(new)
print(d)