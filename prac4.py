import string
def ispangram(Str,a = string.ascii_lowercase):
    aset= set(a)
    Str = Str.replace(' ',' ')
    Str = Str.lower()
    Str = set(Str)
    if aset == Str:
        print('tRUE')
str = input("Enterb a string:")
print(ispangram(str))