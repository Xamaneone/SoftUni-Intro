def password_validator(password):
    password_is_valid = True
    if 6 > len(password) or len(password) > 10:
        password_is_valid = False
        print("Password must be between 6 and 10 characters")
    password.split()
    for letter in password:
        if 48 <= ord(letter) <= 122:
            a = None
        else:
            password_is_valid = False
            print("Password must consist only of letters and digits")
            break
    count = 0
    for letter in password:
        if 45 <= ord(letter) <= 57:
            count += 1
    if count < 2:
        password_is_valid = False
        print(f"Password must have at least 2 digits")
    if password_is_valid is True:
        print("Password is valid")
password_validator(str(input()))