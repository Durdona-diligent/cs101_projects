# The Password Strength 
def validate_password(password):
    if len(password) >= 8:
        if password != password.lower():
            if "password" not in password.lower():
                for char in password:
                    if '1' <= char <= '9':
                        return True
            else:
                return False
        else:
            return False
    else:
        return False
print(validate_password("apple"))           # False (too short)
print(validate_password("Password123"))     # False (contains 'password')
print(validate_password("security"))        # False (no uppercase, no digit)
print(validate_password("SecureCode99"))    # True