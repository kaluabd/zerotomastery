is_magician = False
is_expert = True

if is_expert and is_magician:
    print('you are a master magician')
elif  is_magician and  not is_expert:
    print('at least you are getting there')
elif not is_magician:
    print('you need power')
else:
    pass