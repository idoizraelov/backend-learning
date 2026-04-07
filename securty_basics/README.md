# User Authentication & Security Simulator 

This is a Python script that simulates a secure user registration and login system. It demonstrates the fundamental security concepts used in real-world backend servers to protect user data and prevent hacker attacks.

## Core Features I Built:
1. **Data Validation ("The Bouncer"):** Checks if the user's password is strong enough (minimum 8 characters, at least 1 uppercase letter, 1 number, and 1 special character).
2. **Password Hashing ("The Shredder"):** Uses the professional `bcrypt` library to convert the password into an unreadable string with a random "salt". Passwords are NEVER saved as plain text.
3. **Anti-Brute Force ("Account Lockout"):** A security mechanism that tracks failed login attempts and locks the account after 3 consecutive mistakes.

---

## Real-World Implementation

This script demonstrates the core logic of backend security. However, in a real production environment, the security flow does not end here.

A real system connects to a **Database (like SQL)** to securely save the hashed passwords and permanently track failed login attempts. In addition, production servers use more security layers and functions (like login tokens, CAPTCHAs, and two-factor authentication) to make the system much stronger.


## How to run:
Run the script in the terminal:
`python auth_simulator.py`