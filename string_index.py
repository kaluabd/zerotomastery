# String index positioning is how python store values in order of sequence.
# Example:
    # The following shows how python takes arguments is square bracket
    # [start:stop:stepover] --- It is important to remember this.

name = "parker"
       #012345

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])

numbers = "012345678"
          #012345678

print(numbers[0:9])
print(numbers[0:9:2])
print(numbers[:5])
print(numbers[1:])
print(numbers[::2])
print(numbers[:-1])
print(numbers[::-1])