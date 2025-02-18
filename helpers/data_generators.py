import random
import string

def generate_email(domain="gmail.com"):
    username_length = 8
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=username_length))
    return f"{username}@{domain}"

def generate_password(length=8):
    if length < 4:
        raise ValueError("Пароль должен быть не менее 4 символов.")
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=length))