# Python Banking System

A menu-driven, Python-based mini-project that simulates basic banking
operations for an internship assignment.

## Features

1. **Account Creation** — enter name, phone number, and a 4-digit security PIN
2. **Secure Login** — access using account number and PIN (3 attempts allowed)
3. **Check Balance**
4. **Deposit Money**
5. **Withdraw Money**
6. **Transfer Funds** — to another existing account
7. **View Transaction History** — timestamped log per account
8. **Change PIN**
9. **Logout**

## How to Run

```bash
python3 banking_system.py
```

Requires Python 3 only — no external libraries needed.

## Concepts Used

- Variables, loops (`while`, `for`) and conditional statements (`if`/`elif`/`else`)
- Dictionaries (`accounts`) and lists (`transactions`)
- Functions for each banking operation
- `random` module — to generate unique 6-digit account numbers
- `datetime` module — to timestamp every transaction

## Notes

- All data is stored **in memory** (in the `accounts` dictionary) for the
  duration of the program run, as required by the assignment scope
  (only basic Python concepts — no file/database persistence).
- Account numbers are randomly generated 6-digit numbers, guaranteed unique.
- PINs must be exactly 4 digits.

## Project Structure

```
banking_system/
├── banking_system.py   # Main application (run this file)
└── README.md            # This file
```

## Sample Flow

1. Run the program → choose **1. Create Account**
2. Enter name, phone number, and set a 4-digit PIN
3. Note down the generated account number
4. Choose **2. Login**, enter account number and PIN
5. Use the account menu to deposit, withdraw, transfer funds, view history,
   change PIN, or logout
