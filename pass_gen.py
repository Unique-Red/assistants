from itertools import combinations
import string
import secrets #to get true random numbers

#Create function to generate password
def generate_password(length: int, symbols: bool, uppercase: bool ):
    combination = string.ascii_lowercase + string.digits

    #to allow users decide the kinda password to generate(to include symbol or uppercase)
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
    print(index+1, ":","ilove"+ generate_password(length=10, symbols=True, uppercase=True))