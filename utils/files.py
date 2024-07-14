from .constants import ALPHABET
from random import choice, randint
from hashlib import sha256
from tempfile import NamedTemporaryFile, gettempdir
from os import listdir, remove

def generate_password(pswd: str, salt=None):
    if salt is None:
        salt = ''.join([choice(ALPHABET) for _ in range(randint(8, 15))])
    salted = pswd + salt
    return sha256(salted.encode()).hexdigest(), salt

def get_pswd_hash(login: str):
    try:
        with open('passwords.txt') as f:
            for check_login, pswd in map(str.splitlines, f.read().split("\n\n")): 
                if check_login == login:
                    return pswd
    except FileNotFoundError:
        return None

def get_logins():
    try:
        with open('passwords.txt') as f:
            return f.read().splitlines()[::2]
    except FileNotFoundError:
        return []

def get_salt(login: str):
    try:
        with open('salts.txt') as f:
            for s_login, salt in map(str.split, f.read().split("\n")):
                if s_login == login:
                    return salt
    except FileNotFoundError:
        return None

def add_user(login: str, pswd: str):
    encrypted, salt = generate_password(pswd)
    with open('passwords.txt', 'a',) as pswds:
        pswds.write(f"{login}\n{encrypted}")
    with open('salts.txt', 'a') as salts:
        salts.write(f"{login} {salt}\n")
    add_cache(login, encrypted)

def add_cache(login: str, encrypted: str):
    with NamedTemporaryFile(prefix="cache_", suffix=f"_session", delete_on_close=False, delete=False) as cache:
        cache.write(f"{login}\n{encrypted}".encode())

def search_cache() -> str | None:
    for file in listdir(gettempdir()):
        if file.startswith("cache_") and file.endswith(f"_session"):
            return f'{gettempdir()}\\{file}'
    return None

def get_cache():
    cache = search_cache()
    if cache is None:
        return False
    with open(cache, 'rb') as file:
        login, pswd = file.read().decode().split("\n")
    if pswd == get_pswd_hash(login):
        return login


def remove_cache():
    cache = search_cache()
    if cache is None:
        return ""
    remove(cache)
