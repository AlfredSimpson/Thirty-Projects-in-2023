# Python Password Generator

* Language: Python
* Author: Alfred Simpson
* Created: 2023-03-16
* Updated: 2023-03-16

## Overview

This is a simple python password generator that prompts a user to generate a secure password and provides the entropy/randomness associated with their password.

While creating this, I realized that it might also be helpful to calculate the bits of entropy as well as the current time to brute force the password using traditional means. My crackable method is not perfect - as it only really accounts for entropy and not previous breaches, etc.

### Libraries and Learnings
* random, string, math

## Detailed Development

### Overview of the Code

Section-by-section breakdown

* First we import our modules: random, string, and math
* Second we establish our generate_password() method, which takes length as a parameter.
* * Assign characters the value of all ascii letters, digits, and punctuation
* * Now randomly choose each character up to the length requested. 
* Third, figure out entropy. 
* * Entropy is, essentially, the randomness of a character.
* * This formula needs to know how the complexity (char_set) and the length of your password to figure out the bits of entropy.
* * The complexity is the char_set_length (). 
* * Finally, plug it into the formula.
* * Entropy is equal to the length of the password * the log2(complexity)
* Fourth step: Calculate how long it'd take to brute force the password in crackable().
* * We assume that a computer can do 10[^10]. This is variable. 
* * I chose this number assuming that an attacker has at least a decent GPU to assist in cracking.
* * Calculate the total attempts needed (2 to the power of the entropy)
* * Then figure out time in seconds to crack by dividing the total attempts by the attempts per second.
* Fifth step: format the time.
* * Yes, we could just probably call in another library and save us time, but  hey, let's have fun.
* * Figure out that a year is 60*60*24*365 (no leapyears), a month is 60 seconds * 60 minutes * 24 hours per day * 30 days in a month (forget the rest of the months), etc.
* Store those in a list
* * From here formulate how many years, months, days, hours, minutes, and seconds are spent cracking this on a modest machine.
* Finally: execute the script in main:
* * Have the user provide a password length, raise errors if they don't supply the right value
* * Calculate needed information using the methods above
* * Return the values!

### Known Bugs or missing features
* It'd be nice to specify if you wanted ONLY letters or ONLY numbers or to exclude punctuation, etc. 

### References
* https://stackoverflow.com/questions/54733868/how-many-attempts-per-second-can-a-password-cracker-actually-make
* * This stackoverflow question from 2018 mentions that a 2080Ti can crack 100B hashes per second.  
* *  10[^10] is roughly 10B, or 1/10th the processing power of a GPU that is now significantly outdated. 
* https://cs.brown.edu/courses/csci1660/demos/password-cracking/#:~:text=Benchmarks&text=On%20the%20Sunlab%20machines%20using,several%20million%20passwords%20per%20second.
* * This Brown.Edu course material backs up the statement showing that it is able to hash several million passwords per second.
* https://hackaday.com/2012/12/06/25-gpus-brute-force-348-billion-hashes-per-second-to-crack-your-passwords/
* * And this article stated a right with 25 GPUs across 5 machines to achieve 348B per second
* I chose to be modest and assume they have at least a 3070 ti, which achieves even anywhere from 50k hashes per second to 40-50B hashes per second, and that the attacker didn't dedicate ever ounce of power to the cracking, overclock their machine, or use more than one GPU.
* * Given the evidence and parity of the above, I chose 10B per second as a reasonable and modest amount.
