import random
import string
import json
import os

# File to store mapping
MAPPING_FILE = "letter_mapping.json"

def generate_mapping():
    letters = list(string.ascii_uppercase)
    shuffled = letters.copy()
    random.shuffle(shuffled)
    mapping = dict(zip(letters, shuffled))
    return mapping

def load_or_create_mapping():
    if os.path.exists(MAPPING_FILE):
        with open(MAPPING_FILE, "r") as f:
            return json.load(f)
    else:
        mapping = generate_mapping()
        with open(MAPPING_FILE, "w") as f:
            json.dump(mapping, f)
        return mapping

def encode_password(password, mapping):
    encoded = ""
    for char in password.upper():
        if char in mapping:
            encoded += mapping[char]
        else:
            encoded += char  # leave numbers/symbols unchanged
    return encoded

# --- Usage ---
mapping = load_or_create_mapping()
print("Letter Mapping:", mapping)

password = input("Enter password: ")
print("Encoded Password:", encode_password(password, mapping))
