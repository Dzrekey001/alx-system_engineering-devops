**Current Working Directory and Home Directory Shell Script**
***
This shell script contains two tasks:

Displaying the absolute path name of the current working directory.
Changing the current working directory to the user's home directory.

**Usage**
To run the shell script, follow the steps below:

Open your terminal and navigate to the directory where the script is located.

Make sure the script has execute permission by running the following command:
***
bash

Copy code
chmod +x current_home_dir.sh
To display the absolute path name of the current working directory, run the following command:
***
bash

Copy code
./current_home_dir.sh -p
This will print the absolute path name of the current working directory.
***
To change the current working directory to the user's home directory, run the following command:
***
bash

Copy code
./current_home_dir.sh -c
This will change the current working directory to the user's home directory.
***
Permissions
The script requires execute permission to be run. You can give execute permission to the owner of the file using the chmod command, like so:
***
bash
Copy code
chmod u+x current_home_dir.sh
This will give the owner of the file execute permission. You can also give execute permission to everyone using the following command:
***
bash

Copy code
chmod +x current_home_dir.sh
***

**Notes**
The script was written in bash and has been tested on Ubuntu 22.04 LTS.

The script uses the pwd command to display the current working directory and the cd command to change the current working directory.

The script assumes that the user's home directory is located at /home/username, where username is the name of the current user.
