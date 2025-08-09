# Day 005 – Random Password Generator

## What I Built
A Python program that generates a secure password based on the user’s preferences.  
The user can choose how many **letters**, **symbols**, and **numbers** they want, and the program will generate a randomized password.

## What I Learned
- How to use the `random` module:
  - `random.choice()` to pick random characters
  - `random.shuffle()` to randomize order
- How to store characters in lists for easy selection
- How to collect and validate numeric user input with `int()`
- How to build strings by appending items to a list and then using `"".join()` to combine them

## Hardest Part
Initially, I tried to `.append()` characters to a string instead of a list, which caused errors.  
Also, I accidentally looped over a list instead of the user’s numeric input, which I fixed by referencing `nr_symbols` instead of `symbols`.

## Extra Challenges or Features
- Allowed the user to fully customize the number of letters, symbols, and numbers in their password
- Shuffled the final list to ensure the password is not in predictable order
- Used a wide range of characters including uppercase, lowercase, digits, and special symbols

## Reflection
This project was a great introduction to combining lists, loops, and randomization to create something practical.  
I learned the importance of input validation and the difference between working with strings vs. lists in Python.
