# -*- coding: utf-8 -*-
"""
Caesar cypher script

Encode and decode messages by scrambling the letters in your message

Created on Fri Feb  1 23:06:50 2019

@author: shakes
"""
import string

letters = (
    string.ascii_letters
)  # contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

message = "The quick brown fox jumped over the lazy dog"  # type your message here
print("Message:", message)

# create the Caesar cypher
offset = 5  # choose your shift
totalLetters = 26
keys = {}  # use dictionary for letter mapping
invkeys = (
    {}
)  # use dictionary for inverse letter mapping, you could use inverse search from original dict
for index, letter in enumerate(letters):
    # cypher setup
    if index < totalLetters:  # lowercase
        keys[letter] = letters[(index + offset) % totalLetters]
    else:  # uppercase
        keys[letter] = letters[(index + offset) % totalLetters + totalLetters]

invkeys = {v: k for k, v in keys.items()}  # reverse of letter mapping dictionary

print("Cypher Dict:", keys)

# encrypt
encryptedMessage = []
for letter in message:
    if letter == " ":  # spaces
        encryptedMessage.append(letter)
    else:
        encryptedMessage.append(keys[letter])
print("Encrypted Message:", "".join(encryptedMessage))

# decrypt
decryptedMessage = []
for letter in encryptedMessage:
    if letter == " ":
        decryptedMessage.append(letter)
    else:
        decryptedMessage.append(invkeys[letter])
print("Decrypted Message:", "".join(decryptedMessage))
