# the last daya type from the main one
# set
# set is unordered collection of unique objects
# it is like a dict with out a key and value chains

my_set = {1,2,3,4,5,6,6}
print(my_set) # only print the unique objects, it does not repeat the same objects

my_set.add(100)
my_set.add(3)
print(my_set) # only unique objects are printed
print(len(my_set))


# exercise
exe = [1,2,3,3,4,5,6,6]
print(set(exe))
