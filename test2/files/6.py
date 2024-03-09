import os
import string
strings = string.ascii_uppercase
path_to = r'/Users/apple/Desktop/test2/'
for i in strings:
    with open(f"{i}.txt","w")as file:
        file.write("ff")
    

