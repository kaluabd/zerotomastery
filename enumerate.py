# enumerate shows the index counter of the item we loop through

for char in enumerate("hello"):
    print(char)

    # (0, 'h')
    # (1, 'e')
    # (2, 'l')
    # (3, 'l')
    # (4, 'o')

for i,char in enumerate("hello"):
    print(i, char)
    print('')

    # 0 h
    # 1 e
    # 2 l
    # 3 l
    # 4 o


# Exercise printing the index of the number 50 in the loop
for i, char in enumerate(range(60)):
    if char == 50:
        print(f" the index of num 50 is : {i} ")