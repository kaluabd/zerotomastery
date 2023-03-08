# Tuple
# Tuples are immutable
# It is like a list but can not be changed
# Used to store something that stays without changing.

my_tuple = (1,2,3,4,4,4,5,6)
print(my_tuple)

# Another example
print(my_tuple.count(4)) # counts how many times num 4 is repeated
print(my_tuple.index(3))

# example of dictionary
# Dictinary has a key:value positioning.
user = {
    'name': 'kyle', 
    'age': 25,
    'location': 'London'
}

print(user)
print(user.items())