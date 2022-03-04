from itertools import combinations
import string
import secrets #to get true random numbers

def generate_password(length: int, symbols: bool, uppercase: bool ):
    combination = string.ascii_lowercase + string.digits

    #to allow users decide the kinda password to generate
    if symbols:
        combination += string.punctuation
    if uppercase:
        combination += string.ascii_uppercase

    combination_length = len(combination)

    new_password = ""

    for _ in range(length):
        new_password += combination[secrets.randbelow(combination_length)]

    return new_password

for _, index in enumerate(range(5)):
    print(index+1, ":", generate_password(length=10, symbols=False, uppercase=True))