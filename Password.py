import secrets
import string

def generate_strong_password(length=16, use_uppercase=True, use_digits=True, use_special=True):
    """
    Generate a strong random password.

    Parameters:
        length (int): Length of the password (minimum 8).
        use_uppercase (bool): Include uppercase letters if True.
        use_digits (bool): Include digits if True.
        use_special (bool): Include special characters if True.

    Returns:
        str: A strong random password.
    """
    if length < 8:
        raise ValueError("Password length must be at least 8 characters for security.")
    
    # Base character pool: always include lowercase letters
    char_pool = string.ascii_lowercase
    
    # Add character sets based on user preferences
    if use_uppercase:
        char_pool += string.ascii_uppercase
    if use_digits:
        char_pool += string.digits
    if use_special:
        char_pool += "!@#$%^&*()-_=+[]{}|;:<>,.?/"
    
    if len(char_pool) == 0:
        raise ValueError("No characters available to generate password. Enable at least one character set.")

    # Generate a secure password
    password = ''.join(secrets.choice(char_pool) for _ in range(length))
    
    return password

# Example Usage
if __name__ == "__main__":
    # Customize password parameters as needed
    password_length = 16
    strong_password = generate_strong_password(
        length=password_length,
        use_uppercase=True,
        use_digits=True,
        use_special=True
    )
    print(f"Generated Strong Password: {strong_password}")
