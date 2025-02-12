# -*- coding: utf-8 -*-
"""caeser.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1EKZAvODDW3R3eqHQFSZYcQCwoBZJHFnF
"""

import string

alphabet = list(string.ascii_lowercase)

def caesar_cipher(text, shift, direction):
    shift = shift % 26  # Ensure shift remains within bounds
    result = ""
    for char in text:
        if char.lower() in alphabet:  # Check if character is in alphabet
            new_index = (alphabet.index(char.lower()) + shift) % 26 if direction == "encode" else (alphabet.index(char.lower()) - shift) % 26
            new_char = alphabet[new_index]
            result += new_char.upper() if char.isupper() else new_char
        else:
            result += char  # Keep special characters unchanged
    print(f"The {direction}d text is {result}")

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction not in ['encode', 'decode']:
        print("Invalid option, please enter 'encode' or 'decode'.")
        continue

    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))

    caesar_cipher(text, shift, direction)

    repeat = input("Do you want to repeat? (y/n)\n").lower()
    if repeat != 'y':
        print("OK byee!!")
        break

