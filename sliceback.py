letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[::-1]
print(backwards)

print(letters[-10:-12])

# slice the string to produce qpo
print(letters[16:13:-1])

# slice the string to produce edcba
print(letters[4::-1])

# slice the string to produce the last 8 characters, in reverse order
print(letters[-9:-1])

print(letters[-4:])   # wxyz
print(letters[-1:])   # z
print(letters[:1])   # a