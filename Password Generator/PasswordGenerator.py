from os import system
import string 
from random import choice
from time import sleep
# Strong Password: At least 12 characters long but 14 or more is better.
# A combination of uppercase letters, lowercase letters,
# numbers, and symbols. Not a word that can be found in a dictionary
# or the name of a person, character, product, or organization.

_LOWER = string.ascii_lowercase
_UPPER = string.ascii_uppercase
_DIGITS = string.digits
_PUNCTUATION = string.punctuation

_CHOICES = [_LOWER, _UPPER, _DIGITS, _PUNCTUATION]

def generate_password(length=14):
    while True:
        password = ''.join(
            choice(choice(_CHOICES)) for _ in range(length)
        )

        if any(c in _LOWER for c in password) and any(c in _UPPER for c in password) and \
            any(c in _DIGITS for c in password) and any(c in _PUNCTUATION for c in password):
            return password
        else:
            print(f"Password missing a type, retrying... (was: {password})")
            generate_password()

def acceptance():
        system("cls")
        print("\n\nGenerated password:\n\n\t", generate_password())
        _USER_OUTPUT = input("\n\nDo you want another password to be generated for you? y/n").strip().lower()
        sleep(0.2)
        print("\ngenerating ...")
        if _USER_OUTPUT in ('', 'y', 'yes'):
            acceptance()
        elif _USER_OUTPUT in ('n', 'no'):
            pass
try:
    acceptance()
except Exception as e:
    print(f"the error is: {e}")
