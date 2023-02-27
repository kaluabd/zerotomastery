# Strings in python are immutable
# Example

just_string = '01234'
just_string[0] = '1'
print(just_string[0])


# The above code throws a TypeError saying string object does not support item assignment
# Because of this strings in python are immutable
# The only way to change the value is to create something new 