# Python program to add salting and iteration in given string.
import hashlib
import os

# get string from user
print("Enter string:")
str_data = input()

# generate string of size random bytes using os library
data = os.urandom(60)

# generate sha256 salt
salt = hashlib.sha256(data).hexdigest().encode()

# provide salt and string to pbkdf2_hmac to generate hash
str_hash = hashlib.pbkdf2_hmac('sha512',str_data.encode('utf-8'), salt, 100000)

# print hash value of given string after salting
print("Hash value:",str_hash.hex())