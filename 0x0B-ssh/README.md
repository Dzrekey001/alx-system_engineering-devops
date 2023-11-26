# 0x0B. SSH

## Overview

This project focuses on understanding and implementing SSH (Secure Shell) in a DevOps environment. It covers connecting to a remote server using SSH, creating SSH key pairs, and configuring the SSH client.

## Learning Objectives

By the end of this project, you should be able to:

- Explain what a server is and where servers usually live.
- Understand the basics of SSH.
- Create an SSH RSA key pair.
- Connect to a remote host using an SSH RSA key pair.
- Recognize the advantages of using `#!/usr/bin/env bash` instead of `/bin/bash`.

## Files and Directories

- `0-use_a_private_key`: Bash script to connect to a server using the private key `~/.ssh/school` with the user `ubuntu`.
- `1-create_ssh_key_pair`: Bash script to create an RSA key pair with the private key named `school` (protected by the passphrase `betty`).
- `2-ssh_config`: SSH client configuration file to use the private key `~/.ssh/school` and refuse password authentication.

