# Implementation of simple conditional logic that checks if someone can drive a car or not.

driving_age = 18
driver_licence = 'yes'

age = int(input('age: '))
driver_licence = input('driving licence (yes/no): ')

if age >= 18 and driver_licence == 'yes':
    print('can drive')
else:
    print('can not drive for now!')


# truthy is something that have a value and that value is not zero.
# falsey is when it contains no value or false value and None values.
