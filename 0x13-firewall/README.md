# Project: 0x13-firewall

## Description

This project involves configuring a firewall using UFW (Uncomplicated Firewall) on the web server, web-01. The tasks include blocking all incoming traffic except for specific TCP ports and setting up port forwarding.

## Tasks

### 0. Block all incoming traffic but

- Install UFW firewall on web-01.
- Configure UFW to block all incoming traffic, except for the following TCP ports:
  - 22 (SSH)
  - 443 (HTTPS SSL)
  - 80 (HTTP)
- Share the UFW commands used in the answer file.

### 1. Port forwarding

- Configure web-01 to redirect port 8080/TCP to port 80/TCP.
- Provide the UFW configuration file that was modified to achieve this.
- Include a netstat output on web-01 and demonstrate the port forwarding using curl from web-02.

