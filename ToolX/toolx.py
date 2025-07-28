import os
import time

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
    if choice == '0':
        os.system("python ToolX/subdomain-finder/sub_finder.py")
    elif choice == '1':
        os.system("python ToolX/email-scraper/email_scraper.py")
    elif choice == '2':
        os.system("python ToolX/hash-cracker/hash_cracker.py")
    elif choice == '3':
        os.system("python ToolX/lan-portscanner/lan_portscanner.py")
    elif choice == '4':
        os.system("python ToolX/password-generator/password_generator.py")
    elif choice == '5':
        os.system("python ToolX/SSL-certificate-checker/checker.py")
    elif choice == '6':
        os.system("python ToolX/DNS-record-grabber/dns_record.py")
    elif choice == '7':
        os.system("python ToolX/simple-log-analyzer/analyzer.py")
    elif choice == '8':
        os.system("python ToolX/payload-encoder/encoder.py")
    elif choice == '9':
        os.system("python ToolX/wordlist-generator/word_gen.py")
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

