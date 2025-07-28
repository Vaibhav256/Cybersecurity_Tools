import itertools
import random

def generate_wordlist(keywords, min_len=4, max_len=16, use_symbols=True, use_digits=True, casing='mix'):
    symbols = ['@', '#', '$']
    digits = [str(i) for i in range(10)]

    def apply_casing(word):
        if casing == 'lower':
            return [word.lower()]
        elif casing == 'upper':
            return [word.upper()]
        else:
            return [word.lower(), word.capitalize(), word.upper()]

    def has_consecutive_symbols(word):
        for i in range(len(word) - 1):
            if word[i] in symbols and word[i + 1] in symbols:
                return True
        return False

    # Apply casing to all words in the pool
    pool = []
    for kw in keywords:
        pool += apply_casing(kw.strip())
    if use_symbols:
        pool += symbols
    if use_digits:
        pool += digits

    wordlist = set()

    for i in range(2, 4):  # 2 to 3 elements per password
        for combo in itertools.product(pool, repeat=i):
            candidate = ''.join(combo)
            if min_len <= len(candidate) <= max_len and not has_consecutive_symbols(candidate):
                wordlist.add(candidate)

    return sorted(wordlist)

#  Run the generator
if __name__ == "__main__":
    # Permanent common words
    default_keywords = ['admin', 'guest', 'secure', 'access', 'login', 'system', 'root', 'cyber', 'user', 'hacker', 'zero', 'firewall', 'xploit', 'token', 'data', 'intel', 'alpha', 'net', 'cloud', 'matrix']

    print("\nDefault keywords:")
    print(", ".join(default_keywords))
    print("--> You can add your own keywords to the list to make it personalized.")

    custom_input = input("Add custom keywords (comma-separated), or press Enter to continue: ").strip()
    if custom_input:
        custom_keywords = [w for w in custom_input.split(',') if w]
        keywords = default_keywords + custom_keywords
    else:
        keywords = default_keywords

    wordlist = generate_wordlist(
        keywords,
        min_len=4,
        max_len=16,
        use_symbols=True,
        use_digits=True,
        casing='mix'
    )

    print(f"\n== Displaying 20 relevant words out of {len(wordlist)} total ==")
    for word in wordlist[:20]:
        print(word)

    show_more = input("\nGenerate and display remaining words? (y/n): ").strip().lower()
    if show_more == 'y':
        print("\n== Remaining Words ==")
        for word in wordlist[20:]:
            print(word)
    else:
        print("✓ Done. 20 words displayed.")