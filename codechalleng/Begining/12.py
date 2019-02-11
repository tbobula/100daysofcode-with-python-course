def get_profile(*,name='julian', profession='programmer'):
    return "{name} is a {profession}".format(name=name, profession=profession)




s = get_profile()
print(s)
s = get_profile(name='Tomek')
print(s)
s = get_profile(name='Tomek',profession='software engineer')
print(s)