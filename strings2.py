#                   1
#         012345678901234
parrot = "Norwegian Blue"

print(parrot)

print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])
# we win

print()

print(parrot[-11])
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

print()

print(parrot[3 - 14])
print(parrot[4 - 14])
print(parrot[9 - 14])
print(parrot[3 - 14])
print(parrot[6 - 14])
print(parrot[8 - 14])

# slicing
print(parrot[0:6])   # Norweg
print(parrot[3:5])   # we
print(parrot[0:9])   # Norwegian
print(parrot[:9])   # Norwegian

print(parrot[10:14])   # Blue
print(parrot[10:])   # Blue

print(parrot[:6])   # ian Blue
print(parrot[:6] + parrot[6:])   # Norwegian Blue

print(parrot[:])   # Norweigen Blue

# slicing negative numbers
print(parrot[-4:-2])   # Bl
print(parrot[-4:12])   # Bl

# step in a slice
print(parrot[0:6:2])   # Nre
print(parrot[0:6:3])   # Nw

number = "9,223;372:036 854,775;807"
separators = number[1::4]
print(separators)

values = "".join(char if char not in separators else" " for char in number).split()
print([int(val) for val in values])