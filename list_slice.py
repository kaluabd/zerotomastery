# List slicing is like string slices; however here object of a list is sliced.
# Example:

cart = ['phones','laptops', 3, 3.7]
print(cart[:3])

# Formatting a slice nicely:

awesome_format =[
    'banana',
    'orange',
    'avocad',
    'mango'
]

# Printing sliced list value
print(awesome_format[:2])

#lets check if list is immutable or not
awesome_format[2] = 'lemon'

#Print the updated list value
print(awesome_format)


