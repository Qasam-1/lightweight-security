import re

# Simple password strength checker
# This script checks a password against common rules

def check_password_strength(password: str) -> str:
    if len(password) < 8:
        return "Weak: Too short (min 8 chars)"
    if not re.search(r"[A-Z]", password):
        return "Weak: Missing uppercase letter"
    if not re.search(r"[a-z]", password):
        return "Weak: Missing lowercase letter"
    if not re.search(r"[0-9]", password):
        return "Weak: Missing number"
    if not re.search(r"[@$!%*?&#]", password):
        return "Weak: Missing special character (@$!%*?&#)"
    return "Strong password!"

if __name__ == "__main__":
    pw = input("Enter a password to test: ")
    print(check_password_strength(pw))
