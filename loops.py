# Simple implmentation of loops.

for item in (1,2,3,4,5,6):
    print(item)
print(item) #prints the last character because it comes here after looping to the last character


print("/*******************************")

user = {
    'name': 'Dan',
    'age': 45,
    'can_code': True
}

# most important dictionary methods

for key, value in user.items():
    print(key, value)
    print('')
   

for something in user.values():
    print(something)
    print('')
   


for something in user.values():
    print(something)
    print('')
    
for something in user.keys():
    print(something)
    print('')
  