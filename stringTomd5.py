# Python program to generate md5 hash of given string.
import hashlib

# get string from user
print("Enter string to generate md5 hash:")
str_data = input()

# encode string and generate md5 hash
data = hashlib.md5(str_data.encode())

# print digest value of encoded string
print("Digest value of md5 hash:", data.digest())

# print hexadecimal value of encoded string
print("Hex value of md5 hash   :", data.hexdigest())
