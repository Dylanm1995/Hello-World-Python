string1 = "he's "
string2 = "probably "
string3 = "pining "
string4 = "for the "
string5 = "fjords"

print(string1 + string2 + string3 + string4 + string5)
# or
print("he's " "probably " "pining " "for the " "fjords")

# multiplying a string
print("Hello " * 5)
print("Hello " * (5 + 4))

# adding an integer to a string
print("Hello " * 5 + "4")

# to check if a string is a substring of another
today = "Friday"
print("day" in today)   # True
print("Fri" in today)   # True
print("Thur" in today)   # False
print("parrot" in "fjord")   # False

