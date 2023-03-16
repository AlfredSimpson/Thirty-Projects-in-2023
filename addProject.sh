#!/bin/bash

# Prompt user for input
echo "Enter the primary language of the project:"
read language
echo "Enter the name of the project:"
read project_name
echo "Enter a brief description of the project:"
read project_description

# Get the current date
current_date=$(date +"%Y-%m-%d")

# Create language directory if it doesn't exist
language_dir="$language"
if [ ! -d "$language_dir" ]; then
  mkdir "$language_dir"
fi

# Create project directory if it doesn't exist
project_dir="${language_dir}/${project_name}"
if [ ! -d "$project_dir" ]; then
  mkdir "$project_dir"
fi

# Create README.md with the template
readme="${project_dir}/README.md"
if [ ! -e "$readme" ]; then
  cat > "$readme" <<EOL
#  ${project_name}

* Language: ${language}
* Author: Alfred Simpson
* Created: ${current_date}
* Updated: 

## Overview

${project_description}

### Libraries and Learnings
* 

## Detailed Development

### Overview of the Code
* 

### Known Bugs
* 

### References
* 
EOL
fi
