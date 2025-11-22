import re

password_regex = re.compile(r'^(?!.*\s)(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^\w\s]).{12,}$')

def is_valid_password(password : str) -> bool:
    return bool(password_regex.match(password))