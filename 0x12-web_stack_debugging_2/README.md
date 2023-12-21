#Web Stack Debugging #2

##Overview
This project focuses on debugging and optimizing a web stack. The tasks involve running software as another user, configuring Nginx to run as a non-root user, and providing a concise solution for the configuration issue.

***
Tasks
0. Run software as another user

Description
The script accepts one argument (a username) and runs the whoami command under the specified user.

./0-iamsomeoneelse <username>

***
1. Run Nginx as Nginx
Description
Fix the container configuration so that Nginx is running as the nginx user. The web server should be listening on all active IPs on port 8080.
./1-run_nginx_as_nginx

***
2. 7 lines or less (Advanced)
Description
A concise Bash script that configures Nginx to run as the nginx user, listening on port 8080.
./100-fix_in_7_lines_or_less

