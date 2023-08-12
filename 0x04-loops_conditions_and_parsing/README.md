#0x04. Loops, Conditions, and Parsing
***
This project focuses on practicing shell scripting using loops, conditions, and parsing techniques. It covers various tasks related to DevOps, Shell, and Bash scripting. The project aims to enhance your understanding of creating SSH keys, using different types of loops (for, while, until), implementing if-else and case statements, utilizing comparison operators, and working with the cut command.
***
**Learning Objectives**
By completing this project, you will gain knowledge and be able to explain the following topics:

**Creating SSH keys**

Advantages of using #!/usr/bin/env bash over #!/bin/bash
Working with while, until, and for loops
Implementing if, else, elif, and case condition statements
Utilizing the cut command
Understanding file and other comparison operators and their usage
Writing portable scripts

***
**Requirements**

Allowed editors: vi, vim, emacs
All files will be interpreted on Ubuntu 20.04 LTS
All files should end with a new line
A README.md file at the root of the project folder is mandatory
All Bash script files must be executable
You are not allowed to use awk
Your Bash scripts must pass Shellcheck (version 0.7.0) without any error
The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
The second line of all your Bash scripts should be a comment explaining what the script does
***

#Tasks

Task 0: Create a SSH RSA key pair
In this task, you will generate an RSA key pair and share the public key in the provided answer file. You need to keep the private key secure and save it in a reliable location. The public key should also be added to the SSH public key field in your intranet profile.

Task 1: For Best School loop
Write a Bash script that displays the string "Best School" ten times using a for loop.

Task 2: While Best School loop
Write a Bash script that displays the string "Best School" ten times using a while loop.

Task 3: Until Best School loop
Write a Bash script that displays the string "Best School" ten times using an until loop.

Task 4: If 9, say Hi!
Write a Bash script that displays the string "Best School" ten times, but on the ninth iteration, it should display "Hi" on a new line.

Task 5: 4 bad luck, 8 is your chance
Write a Bash script that loops from 1 to 10 and displays different messages based on the iteration number. It should display "bad luck" for the fourth iteration, "good luck" for the eighth iteration, and "Best School" for all other iterations.

Task 6: Superstitious numbers
Write a Bash script that displays numbers from 1 to 20 and shows different messages for specific iterations. It should display "4 and then bad luck from China" for the fourth iteration, "9 and then bad luck from Japan" for the ninth iteration, and "17 and then bad luck from Italy" for the seventeenth iteration. For other iterations, it should display only the number.

Task 7: Clock
Write a Bash script that displays the time for 12 hours and 59 minutes. It should display hours from 0 to 12 and minutes from 1 to 59.

Task 8: For ls
Write a Bash script that lists the content of the current directory in a specific format. It should only display the part of the name after the first dash (-) in each file's name.

Task 9: To file, or not to file
Write a Bash script that gives information about a file. It should display "The file exists" if the file exists, "The file does not exist" if it does not exist, and "Unknown" if the script cannot verify if the file exists.

Task 10: FizzBuzz
Write a Bash script that displays numbers from 1 to 100. It should display "Fizz" for multiples of 3, "Buzz" for multiples of 5, and "FizzBuzz" for multiples of both 3 and 5.

Task 11: Read and cut
Write a Bash script that takes a list of countries as input and displays only their names. The input will be in the format "number: name" (e.g., "1: China", "2: Japan", etc.). The script should display only the names.
