 🔐 Custom Letter-to-Letter Password Generator

This project is a simple **substitution-based password generator** built in Python.  
Each letter `A–Z` is randomly assigned to another letter (e.g., `A=Q`, `B=O`, …).  
This mapping is stored and reused, so the same input always generates the same output.

---

## 🚀 Features
- Randomly generates a **unique letter mapping** the first time you run it.
- Saves the mapping in `letter_mapping.json` so passwords stay consistent.
- Encodes any password you enter by replacing its letters with mapped ones.
- Leaves numbers, spaces, and symbols unchanged.
- Simple and lightweight.

---

## 📂 Project Structure

password-generator/
│── password_generator.py # Main script
│── letter_mapping.json # Stores the generated mapping
│── README.md # Documentation


---

## ⚙️ How It Works
1. On the first run, a random mapping for letters `A–Z` is created.  
   Example:

A → Q
B → O
C → Z
...

2. The mapping is saved in `letter_mapping.json`.  
3. Whenever you type a password like:

tree

It will output something like:

XZPP

(depending on your generated mapping).

---

## ▶️ Usage

1. Clone or download this repo.
2. Run the script:
```bash
python password_generator.py

    Enter your password when prompted:

Enter password: tree
Encoded Password: XZPP

The same password will always encode to the same result as long as you use the same letter_mapping.json.
