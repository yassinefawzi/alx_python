def validate_password(password):
    if ' ' in password:
        return (False)
    if len(password) < 8:
        return (False)
    low = any(char.islower() for char in password)
    up = any(char.isupper() for char in password)
    num = any(char.isdigit() for char in password)

    return low and up and num