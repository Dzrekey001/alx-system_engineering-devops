## Introduction
This project focuses on implementing HTTPS SSL and configuring web servers and load balancers to securely handle web traffic. It explores concepts such as SSL termination, HAProxy configuration, and enforcing HTTPS traffic.

## Concepts
- DNS
- Web stack debugging

## Background Context
Understanding the importance of securing website traffic and implementing HTTPS SSL for encrypted communication.

## Tasks

### 0. World wide web
Configure the domain zone to point subdomains to the corresponding server IP addresses. Create a Bash script that audits subdomains and displays information about them.

**Requirements:**
- Add subdomain www to the domain, pointing it to lb-01 IP.
- Add subdomains lb-01, web-01, and web-02 to the domain, pointing them to the respective server IPs.
- Bash script accepts domain and subdomain parameters.
- Display information for specified subdomain or default subdomains (www, lb-01, web-01, web-02).
- Output format: 'The subdomain [SUB_DOMAIN] is a [RECORD_TYPE] record and points to [DESTINATION]'.
- Use awk and at least one Bash function.

### 1. HAproxy SSL termination
Configure HAProxy to handle SSL termination for the www subdomain.

**Requirements:**
- HAProxy listening on port TCP 443.
- HAProxy accepting SSL traffic.
- HAProxy serving encrypted traffic that returns the root of the web server.
- When querying the root of the domain, the page should contain 'Holberton School'.
- Install HAProxy 1.5 or higher.
- Share HAProxy config as '/etc/haproxy/haproxy.cfg'.

### 2. No loophole in your website traffic
Enhance security by configuring HAProxy to automatically redirect HTTP traffic to HTTPS.

**Requirements:**
- Transparent redirection for the user.
- HAProxy returning a 301.
- HAProxy redirecting HTTP traffic to HTTPS.
- Share updated HAProxy config as '/etc/haproxy/haproxy.cfg'.

## Quiz Questions
1. What are the two main roles of HTTPS SSL?
2. What is the purpose of encrypting traffic in SSL?
3. What does SSL termination mean?

## Your Servers
| Name           | Username | IP               | State   |
| -------------- | -------- | ----------------- | ------- |
| 98481-web-01   | ubuntu   | 100.26.215.202   | running |
| 98481-web-02   | ubuntu   | 100.25.199.235   | running |
| 98481-lb-01    | ubuntu   | 54.237.33.100    | running |
