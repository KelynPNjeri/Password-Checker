"""Password Checker."""
import re


def validate_password(password):
    """
    Validating Password.
    """
    # password = input("Please enter Password:")
    if (len(password) < 6) or (len(password) > 12):
        return "Invalid Password"
    elif not re.search("[A-Z]", password):
        return "Invalid Password"
    elif not re.search("[a-z]", password):
        return "Invalid Password"
    elif not re.search("[0-9]", password):
        return "Invalid Password"
    elif not re.search(r"[^\w\*]", password):
        return "Invalid Password"
    elif not re.search(r"[^\s]", password):
        return "Invalid Password"
    else:
        return "Valid Password"
