# Python program to generate hashes of string data using 3 algorithm from hashlib.
import hashlib

# get string from user
print("Enter string to generate hash:")
str_data = input()

# encode string and generate sha256 hash, shake_256 hash and sha512 hash.
sha256 = hashlib.sha256(str_data.encode())

shake_256 = hashlib.shake_256(str_data.encode())

sha512 = hashlib.sha512(str_data.encode())

# print digest value of encoded string
print("Digest value of sha256 hash   :", sha256.digest())
print("Digest value of shake_256 hash:", shake_256.digest(15))
print("Digest value of sha512 hash   :", sha512.digest())
print("-------------------------------")

# print hexadecimal value of encoded string
print("Hex value of sha256 hash      :", sha256.hexdigest())
print("Hex value of shake_256 hash   :", shake_256.hexdigest(15))
print("Hex value of sha512 hash      :", sha512.hexdigest())
