# -*- coding: utf-8 -*-
"""
Determine the shift of the Caesar Cypher

Created on Sat Feb  2 23:03:02 2019

@author: shakes
"""
from collections import Counter
import string

message = "Z lzm zmc z okzm"
# frequency of each letter
letter_counts = Counter(message)
# print(letter_counts)
print(letter_counts)

# find max letter
maxFreq = -1
maxLetter = None
for letter, freq in letter_counts.items():
    print(letter, ":", freq)
    # INSERT CODE TO REMEMBER MAX
    if freq > maxFreq:
        if letter == " ":
            pass
        else:
            maxFreq = freq
            maxLetter = letter

print("Max Ocurring Letter:", maxLetter)

# predict shift
letters = (
    string.ascii_letters
)  # contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

most_common_letters = ["e", "a", "r", "i", "o", "t", "n", "s", "l", "c"]

for common_letter in most_common_letters:
    shift = abs((letters.find(maxLetter) - letters.find(common_letter)) % 26)

    totalLetters = 26
    keys = {}  # use dictionary for letter mapping

    offset = 26 - shift

    for index, letter in enumerate(letters):
        # decryption setup
        if index < totalLetters:  # lowercase
            keys[letter] = letters[(index + offset) % totalLetters]
        else:  # uppercase
            keys[letter] = letters[(index + offset) % totalLetters + totalLetters]

    decryptedMessage = []

    # decrypting
    for letter in message:
        if letter == " ":  # spaces
            decryptedMessage.append(letter)
        else:
            decryptedMessage.append(keys[letter])

    print("Predicted Shift:", shift)
    print("Decrypted Message:", "".join(decryptedMessage))

    # checking if message is correct
    user_input = input("Is this the correct message? y/n ")

    if user_input in ("y", "Y"):
        break
