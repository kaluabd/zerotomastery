#A simple password length checker

usrnm = input('username: ')
psswd = input('password: ')

#Printing the username and password

psswd = len(psswd)
psswd = '*' * psswd

#printing some new lines
print('')
print('')

print(f'your username is: {usrnm} ')
print(f'your password is: {psswd}')