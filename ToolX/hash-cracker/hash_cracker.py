import hashlib
import os

def detect_hash_type(hash_val):
    length = len(hash_val)
    if length == 32:
        return 'md5'
    elif length == 40:
        return 'sha1'
    elif length == 64:
        return 'sha256'
    else:
        return None

def crack_hash(hash_to_crack, wordlist_path_input):
    hash_type = detect_hash_type(hash_to_crack)

    if not hash_type:
        print(f"[!] Unable to detect hash type. Unsupported or invalid hash length: {len(hash_to_crack)}")
        return
    else:
        print(f"[+] Detected hash type: {hash_type.upper()}")

    # Hybrid path handling
    if os.path.isfile(wordlist_path_input):
        wordlist_path = wordlist_path_input
    else:
        script_dir = os.path.dirname(__file__)
        wordlist_path = os.path.join(script_dir, wordlist_path_input)
        if not os.path.isfile(wordlist_path):
            print(f"[!] Wordlist file '{wordlist_path_input}' not found.")
            return

    try:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
            passwords = f.readlines()
    except Exception as e:
        print(f"[!] Failed to open wordlist: {e}")
        return

    print(f"[+] Loaded {len(passwords)} passwords from wordlist.\n")

    for password in passwords:
        password = password.strip()
        hashed = ''
        if hash_type == 'md5':
            hashed = hashlib.md5(password.encode()).hexdigest()
        elif hash_type == 'sha1':
            hashed = hashlib.sha1(password.encode()).hexdigest()
        elif hash_type == 'sha256':
            hashed = hashlib.sha256(password.encode()).hexdigest()

        if hashed == hash_to_crack.lower():
            print(f"[✔] Password found: {password}")
            return

    print("[✘] Password not found in wordlist.")

# --- Main ---
if __name__ == '__main__':
    print("🔐 Simple Hash Cracker with Auto Detection\n")

    hash_input = input("Enter the hash to crack: ").strip().lower()
    wordlist = input("Enter path to wordlist (e.g., rockyou.txt): ").strip()

    crack_hash(hash_input, wordlist)
