# Program Password Generator

import random
import string

print(20*"==")
print("Password Generator")
print(20*"==")

main_pass = input("masukkan main password anda : ")

# password_characters = string.ascii_letters + string.digits + string.punctuation

def randomizer_1(length):
    password_characters = string.digits
    password = ''.join(random.choice(password_characters) for i in range(length))
    return password

# format main + number
print(f"randomizer 1 : {main_pass}{randomizer_1(3)}")
# format number + main
print(f"randomizer 2 : {randomizer_1(3)}{main_pass}")


def randomizer_2(length):
    password_characters = string.ascii_letters
    password = ''.join(random.choice(password_characters) for i in range(length))
    return password

# format main + number
print(f"randomizer 3 : {main_pass}{randomizer_2(3)}")
# format number + main
print(f"randomizer 4 : {randomizer_2(3)}{main_pass}")

def randomizer_3(length):
    password_characters = string.punctuation
    password = ''.join(random.choice(password_characters) for i in range(length))
    return password

# format main + number
print(f"randomizer 5 : {main_pass}{randomizer_3(3)}")
# format number + main
print(f"randomizer 6 : {randomizer_3(3)}{main_pass}")

def randomizer_4(length):
    password_characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(password_characters) for i in range(length))
    return password

# format main + number
print(f"randomizer 7 : {main_pass}{randomizer_4(3)}")
# format number + main
print(f"randomizer 8 : {randomizer_4(3)}{main_pass}")

def randomizer_5(length):
    password_characters = string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for i in range(length))
    return password

# format main + number
print(f"randomizer 9 : {main_pass}{randomizer_5(3)}")
# format number + main
print(f"randomizer 10: {randomizer_5(3)}{main_pass}")