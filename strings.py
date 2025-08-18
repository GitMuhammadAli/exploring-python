def swap(a, b):
    a, b = b, a
    return a, b
x = 2
y = 4
x, y = swap(x, y)
print(f"x is now {x} and y is now {y}")

another = "Shahid"
course = '''

hi my name is ali

i am new python dev at hubble42
'''
print(course)
print(course[-1])
print(another[1:-1])


first = "ali"
second = "shahid"


print(f'{first} whos is son of {second} is a python dev')



#--------------- STRING METHODS--------------------#

print(len(first))
print("ali" in first)