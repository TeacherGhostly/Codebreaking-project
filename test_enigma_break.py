# -*- coding: utf-8 -*-
"""
Create and test an Enigma machine encryption and decoding machine

This code is based on the implementation of the Enigma machine in Python 
called pyEnigma by Christophe Goessen (initial author) and Cédric Bonhomme
https://github.com/cedricbonhomme/pyEnigma

Created on Tue Feb  5 12:17:02 2019

@author: uqscha22
"""
import string
import enigma
import rotor
import time

letters = (
    string.ascii_letters
)  # contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
capitalLetters = letters[-26:]
# print(capitalLetters)

ShakesHorribleMessage = "Xm xti ca idjmq Ecokta Rkhoxuu! Kdiu gm xex oft uz yjwenv qik parwc hs emrvm sfzu qnwfg. Gvgt vz vih rlt ly cnvpym xtq sgfvk jp jatrl irzru oubjo odp uso nsty jm gfp lkwrx pliv ojfo rl rylm isn aueuom! Gdwm Qopjmw!"
crib = "Hail Shakes!"
crib_substring = ShakesHorribleMessage[-12:]
print(crib_substring)

##Break the code via brute force search
# INSERT CODE HERE
decoded_message = ""
message_found = False
attempt_count = 0

start_time = time.time()  # Start the timer

# Iterate from AAA to ZZZ as the key
for letter1 in capitalLetters:
    if message_found:
        break
    for letter2 in capitalLetters:
        if message_found:
            break
        for letter3 in capitalLetters:
            attempt_count += 1
            potential_key = letter1 + letter2 + letter3

            engine = enigma.Enigma(
                rotor.ROTOR_Reflector_A,
                rotor.ROTOR_I,
                rotor.ROTOR_II,
                rotor.ROTOR_III,
                key=potential_key,
                plugs="AA BB CC DD EE",
            )

            # Decoding based on each combo of AAA to ZZZ, and checking if the crib is correct
            decoded_message = engine.encipher(ShakesHorribleMessage)
            if decoded_message[-12:] == crib:
                message_found = True
                break

end_time = time.time()  # End the timer

runtime = end_time - start_time  # Calculate the runtime

# Print the Decoded message
# INSERT CODE HERE
print("Decoded message: ", decoded_message)
print("Attempt count: ", attempt_count)
print("Time taken: ", runtime)
