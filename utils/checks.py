from re import search
from .constants import *
from .files import get_logins


def check_password(pswd: str) -> bool:
    return search(PASSWORD_REGEX, pswd) is not None

def is_registered(login: str) -> bool:
    return login in get_logins()

def check_login(login: str) -> bool:
    return search(LOGIN_REGEX, login) is not None

def check_user(login: str, pswd: str, retype_pswd: str) -> bool:
    if pswd != retype_pswd:
        print(WRONG_RETYPE)
        return False
    if is_registered(login):
        print(REGISTERED)
        return False
    if not check_login(login):
        print(WRONG_LOGIN)
        return False
    if not check_password(pswd):
        print(WRONG_PASSWORD)
        return False
    return True
