import re

password_reg = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^\w\s]).{12,}$')

def is_valid_password(password : str) -> bool:
    return bool(password_reg.match(password))