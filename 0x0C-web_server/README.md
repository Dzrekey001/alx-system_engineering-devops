#Web Server Configuration Project
This project involves configuring a web server on an Ubuntu machine using Nginx. 
The tasks include transferring files, installing Nginx, setting up a domain name, implementing redirection, and creating a custom 404 page.

***
**Task 0: Transfer a File to Your Server**
Write a Bash script that transfers a file from the client to the server. 
The script should accept the path to the file, the server's IP, the username for the scp connection, and the path to the SSH private key. Usage information is displayed if fewer than three parameters are provided.

**Task 1: Install Nginx Web Server**
Write a Bash script that installs Nginx on the web-01 server. Nginx should be configured to listen on port 80, and a GET request to the root should return a page containing the string "Hello World!"***

**Task 2: Setup a Domain Name**
Provide a domain name (without subdomain) and configure DNS records with an A entry to point to the web-01 server's IP address. Enter the domain name in the Project website URL field in your profile.

**Task 3: Redirection**
Configure Nginx to redirect requests to /redirect_me to another page using a "301 Moved Permanently" redirection.

**Task 4: Not Found Page 404**
Configure Nginx to have a custom 404 page that returns an HTTP 404 error code and contains the string "Ceci n'est pas une page."
