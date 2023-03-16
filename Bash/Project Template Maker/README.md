# Project Template Maker

* Language: Bash
* Created: 2023-03-16
* Updated: 2023-03-16
* * Time to complete: 20 minutes

## Overview

This creates a directory for a  project as well as a directory for the primary language used, if it didn't already exist.

### Libraries and Learnings
* None, just used Bash

## Detailed Development

### Overview of the Code
* This is a pretty straight forward code
* We use a shebang, linking to where my bash script is stored.
* Rather than relying on memorization that a script does something, I instead crafted this to prompt a user for input, and then read the response as a variable.
* I get the current date, the date this script was ran, in a YYYY/MM/DD format
* Next we create a directory for the language if one did not already exist. This is important so that we don't overwrite existing languages or encounter errors while creating future projects in the same language.
* * if starts the if statement.
* * We then check if the directory exists already using: if ! -d "$language_dir" 
* * ! -d [dir name] essentially says "if there's no directory with that name, then...
* * If no directory existed, it creates one.
* * fi ends the if statement.
*  Next up, we create the project directory inside of the language directory.
* * Like with the language directory, we check to make sure that no project directory of this name already exists.
* Finally, we generate a readme for the project inside of the project directory, filled out with a basic template.


### Known Bugs
* None that I'm aware of.

### References
* None
