# LAN Port Scanner

A simple port scanner that checks for open ports on one or more target IP addresses within a specified range. It uses Python's `socket` library to perform the scanning and `termcolor` for colored output in the terminal. This scanner supports scanning multiple targets and offers a spinner animation to indicate progress.

## Features:
- Scan a single or multiple targets.
- Specify the number of ports to scan (from 1 to 65535).
- Colored output to indicate whether a port is open or closed.
- Spinner animation while scanning to show progress.

## Prerequisites:
Ensure you have Python 3.x installed. The script uses the following libraries:
- `termcolor` (third-party)
- Built-in Python libraries:
    - `socket`
    - `itertools`
    - `sys`
    - `time`
    - `re`

## Installation:
1. Clone this repository:

    git clone https://github.com/Vaibhav256/Cybersecurity_Tools/lan-portscanner

2. Install the required dependencies by running:
    
    pip install -r requirements.txt
    

## Usage:
### To run the port scanner:
1. Open a terminal and navigate to the directory containing the script.

    cd /path to/lan-portscanner

2. Run the following command:
    
    python lan_portscanner.py
    

### Example:

'[*]' Enter Targets to Scan (split them by commas): 192.168.0.1,192.168.0.2  
'[*]' Enter the number of ports to scan: 1024
