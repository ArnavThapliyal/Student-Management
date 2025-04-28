"""
Validation functions for student data.
"""

import re

def validate_roll(roll: str) -> bool:
    """Validate the roll number format."""
    pattern = r'^[A-Z]{2}\d{2}[A-Z]{2}\d{3}$'
    return bool(re.match(pattern, roll))

def validate_email(email: str) -> bool:
    """Validate the email format."""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))
