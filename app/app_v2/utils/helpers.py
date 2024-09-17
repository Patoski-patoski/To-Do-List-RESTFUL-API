# app/app_v2/utils/helpers.py
# You can add any helper functions that are reusable across routes

import bcrypt
def validate_email_format(email: str) -> bool:
    """Validate email format using a regex"""
    # Simplistic email regex for demo purposes
    import re

    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

def generate_hashed_password(password: str) -> str:
    """Create a hashed version of password
    Args:
        password (str): password to be hashed
    Returns:
        str: string representation of hashed password
    """
    password = password.encode()
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password, salt)
    return hashed_password


def verify_password(password: str, hashed_password: bytes) -> bool:
    """Verify if a password matches a hashed password
    Args:
        password (str): password to be verified
    Returns:
        bool: True, Otherwise False
    """
    password = password.encode()
    return bcrypt.checkpw(password, hashed_password)
