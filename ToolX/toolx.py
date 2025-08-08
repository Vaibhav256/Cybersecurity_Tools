import os
import time
import subprocess

def banner():
    print(r'''
         ___________  ______      ______    ___       ___  ___       ______   ___  ___  _______    _______   _______   
        ("     _   ")/    " \    /    " \  |"  |     |"  \/"  |     /" _  "\ |"  \/"  ||   _  "\  /"     "| /"      \  
        )__/  \\__/// ____  \  // ____  \ ||  |      \   \  /     (: ( \___) \   \  / (. |_)  :)(: ______)|:        | 
            \\_ /  /  /    ) :)/  /    ) :)|:  |       \\  \/       \/ \       \\  \/  |:     \/  \/    |  |_____/   ) 
            |.  | (: (____/ //(: (____/ //  \  |___    /\.  \       //  \ _    /   /   (|  _  \\  // ___)_  //      /  
            \:  |  \        /  \        /  ( \_|:  \  /  \   \     (:   _) \  /   /    |: |_)  :)(:      "||:  __   \  
            \__|   \"_____/    \"_____/    \_______)|___/\___|     \_______)|___/     (_______/  \_______)|__|  \___) 
                                                                                                                 
                                                    ToolX Cyber Suite v1.0
                                                                                            Built by Vaibhav256
''')


def show_menu():
    print("\nSelect a tool to run:")
    print("0. Subdomain Finder")
    print("1. Email Scraper")
    print("2. Hash Cracker")
    print("3. LAN Port Scanner")
    print("4. Password Generator")
    print("5. SSL Certificate Checker")
    print("6. DNS Record Grabber")
    print("7. Simple Log Analyzer")
    print("8. Payload Encoder")
    print("9. Wordlist Generator")
    print("q. Exit")

def run_tool(choice):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    tool_paths = {
        '0': os.path.join(base_dir, "ToolX", "subdomain-finder", "sub_finder.py"),
        '1': os.path.join(base_dir, "ToolX", "email-scraper", "email_scraper.py"),
        '2': os.path.join(base_dir, "ToolX", "hash-cracker", "hash_cracker.py"),
        '3': os.path.join(base_dir, "ToolX", "lan-portscanner", "lan_portscanner.py"),
        '4': os.path.join(base_dir, "ToolX", "password-generator", "password_generator.py"),
        '5': os.path.join(base_dir, "ToolX", "SSL-certificate-checker", "checker.py"),
        '6': os.path.join(base_dir, "ToolX", "DNS-record-grabber", "dns_record.py"),
        '7': os.path.join(base_dir, "ToolX", "simple-log-analyzer", "analyzer.py"),
        '8': os.path.join(base_dir, "ToolX", "payload-encoder", "encoder.py"),
        '9': os.path.join(base_dir, "ToolX", "wordlist-generator", "word_gen.py")
    }

    if choice in tool_paths:
        try:
            result = subprocess.run(
                ["python", tool_paths[choice]],
                check=True,
                capture_output=True,  # Optional: captures stdout/stderr
                text=True              # Optional: returns output as string
            )
            print(result.stdout)       # Show tool output
        except KeyboardInterrupt:
            print("\n[!] Tool interrupted by user. Returning to menu...")
            time.sleep(1)
        except subprocess.CalledProcessError as e:
            print(f"\n[!] Tool exited with error code {e.returncode}")
            print(f"[!] Error output:\n{e.stderr}")
    elif choice == 'q':
        print("\n[!] Exiting... Stay secure....")
        time.sleep(1)
        exit()
    else:
        print("\n[!] Invalid choice. Try again.")

if __name__ == '__main__':
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        banner()
        show_menu()
        choice = input("\nEnter your choice: ")
        run_tool(choice)
        input("\n[Press Enter to return to menu...]")

