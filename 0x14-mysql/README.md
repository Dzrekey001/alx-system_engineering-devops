#0x14. MySQL
***
##Overview
This project involves setting up MySQL databases, creating replicas, and implementing backup strategies. The tasks cover installing MySQL, creating users, configuring replication, and implementing a backup system.
***
##Learning Objectives
After completing this project, you should be able to explain:

1. The main role of a database
2. What a database replica is and its purpose
3. Why database backups need to be stored in different physical locations
4. Operations to regularly perform to ensure database backup strategy effectiveness
***
##Tasks
0. Install MySQL
Install MySQL 5.7.x on both web-01 and web-02 servers.

1. Let us in!
Create a MySQL user named holberton_user on both web-01 and web-02 with the host name set to localhost and the password projectcorrection280hbtn. Ensure the user has permission to check the primary/replica status.

2. If only you could see what I've seen with your eyes
Create a database named tyrell_corp on web-01, create a table named nexus6, and add at least one entry. Grant SELECT permissions to holberton_user.

3. Quite an experience to live in fear, isn't it?
On web-01, create a new user for the replica server named replica_user with host %. Grant the necessary permissions and ensure holberton_user has SELECT privileges on mysql.user.

4. Setup a Primary-Replica infrastructure using MySQL
Set up primary-replica synchronization with web-01 as the primary MySQL server and web-02 as the replica.

5. MySQL backup
Write a Bash script that generates a MySQL dump and creates a compressed archive. The script should accept a password as an argument.
