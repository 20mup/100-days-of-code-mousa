# Day 004 – Rock, Paper, Scissors Game

## What I Built
A terminal-based Rock, Paper, Scissors game where the user plays against the computer.  
The game uses **randomization**, **input handling**, **lists**, and **conditional logic** to simulate the experience.

## What I Learned
- How to use the `random` module to simulate unpredictable computer choices
- How to store related content (ASCII art) in a list and access it by index
- How to validate user input safely before using it
- The importance of ordering checks to prevent runtime errors (like `IndexError`)
- Cleanly handling draw, win, and loss conditions with compound logical statements

## Hardest Part
At first, the input validation was tricky — using the user’s input as a list index before checking if it was valid caused crashes (`IndexError`).  
Fixing this required checking the input type **and value range** *before* doing anything with it.

## Extra Challenges or Features
- Added detailed ASCII art for each choice
- Built input protection against invalid numbers and non-integer entries
- Improved user experience with clearer prompts and structured output

## Reflection
This was a fun and fast-paced project that tied together a lot of beginner-friendly Python concepts.  
Focusing on code safety and order of execution helped prevent hidden bugs.  
It's a great example of how small games can teach solid software design practices!
