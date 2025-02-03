import random
import string

def generate_password(length):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    characters = letters + digits + symbols
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols)
    ]
    password += random.choices(characters, k = length - 3)
    random.shuffle(password)
    return ''.join(password)

try:
    length = int(input('Enter the password length: '))

    if length < 4:
        print('Length of password should be atleast 4 for security concerns.')
    else :
        print('Generated Password is: ', generate_password(length))

except ValueError:
    print('Invalid Input!! Enter only numeric value.')

