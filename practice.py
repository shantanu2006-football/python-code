def is_strong_password(password):
    if len(password)<8:
        return False
    elif not any(char.isdigit() for char in password):
        return False
    elif not any(char.lower() for char in password):
        return False
    elif not any(char.upper() for char in password):
        return False
    return True
 ##calling this function
print(is_strong_password("wEak"))
print(is_strong_password("Str1n!adfg"))
