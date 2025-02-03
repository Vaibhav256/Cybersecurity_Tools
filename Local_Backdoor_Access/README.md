# Local_Backdoor_Access

The **Local_Backdoor_Access** project is a simple yet powerful toolset for remote command execution and file transfer between a client and a server using Python. This tool enables a backdoor connection between a client and a server, allowing remote command execution, file uploads, and downloads over a socket connection.

> **Note:** This tool should only be used in ethical penetration testing scenarios or with explicit permission. Unauthorized use is illegal.

## Features

- **Remote Shell Access:** Control a remote system via a command shell.
- **File Upload and Download:** Transfer files between the client and the server.
- **Clear Command:** Clear the terminal screen on the client or server.
- **Custom Directory Navigation:** Change directories on the target machine.

## How It Works

- **Client:** The client (backdoor.py) attempts to establish a connection to the server (server.py) every 20 seconds. Once connected, it can execute commands, upload/download files, and return results to the server.
  
- **Server:** The server (server.py) listens for incoming client connections. Once connected, it allows you to send commands, upload files to the client, and download files from the client.

### Usage

#### Setting Up the Server

1. Clone the repository:
   
   git clone https://github.com/Vaibhav256/Cybersecurity_Tools/Local_Backdoor_Access
   cd Local_Backdoor_Access
