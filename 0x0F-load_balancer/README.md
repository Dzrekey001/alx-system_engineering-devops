# Load Balancer Project

## Overview

# This project aims to improve the web stack by adding redundancy to the web servers. 
# The goal is to double the number of web servers, allowing the infrastructure to handle more traffic and enhance reliability. 
# The web servers are placed behind a load balancer to distribute incoming requests.

## Server Information

### Web Servers

1. **Web Server 01**
   - Name: 98481-web-01
   - Username: ubuntu
   - IP: 100.26.215.202
   - State: Running

2. **Web Server 02**
   - Name: 98481-web-02
   - Username: ubuntu
   - IP: 100.25.199.235
   - State: Running

### Load Balancer

1. **Load Balancer 01**
   - Name: 98481-lb-01
   - Username: ubuntu
   - IP: 54.237.33.100
   - State: Running

## Tasks

### Task 0: Double the Number of Webservers

#### Requirements:

- Configure Nginx on web-02 to be identical to web-01.
- Add a custom Nginx response header named `X-Served-By`.
- The value of the custom header must be the hostname of the server Nginx is running on.
- Write a Bash script (`0-custom_http_response_header`) to configure a new Ubuntu machine according to the specified requirements.

#### Example:

```bash
# Check custom header on web-01
curl -sI 34.198.248.145 | grep X-Served-By
# Output: X-Served-By: 03-web-01

# Check custom header on web-02
curl -sI 54.89.38.100 | grep X-Served-By
# Output: X-Served-By: 03-web-02
