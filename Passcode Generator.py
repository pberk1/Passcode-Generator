import random
import string
def create_code(length= 15):
    char= string.ascii_letters + string.digits + string.punctuation
    code= ''.join((random.choice(char)) for i in range(length))
    return code
length= int(input("enter the passcode length: "))
code= create_code(length)
print(f"create code: {code}")