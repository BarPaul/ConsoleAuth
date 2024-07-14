from getpass import getpass
from utils.checks import check_user, is_registered
from utils.files import generate_password, add_user, get_salt, get_pswd_hash, add_cache
from utils.constants import INPUT_LOGIN, INPUT_PASSWORD, INPUT_RETYPE, SUCCESS_REG, NOT_REGISTERED, SUCCESS_AUTH, FAIL_AUTH

def register_user():
    login, pswd, retype_pswd = input(INPUT_LOGIN), getpass(INPUT_PASSWORD), getpass(INPUT_RETYPE)
    print()
    if not check_user(login, pswd, retype_pswd):
        return
    add_user(login, pswd)
    print(SUCCESS_REG)

def authorize_user():
    login, pswd = input(INPUT_LOGIN), getpass(INPUT_PASSWORD)
    if not is_registered(login):
        print(NOT_REGISTERED)
        return authorize_user
    encrypted, _ = generate_password(pswd, get_salt(login))
    if get_pswd_hash(login) == encrypted:
        print(SUCCESS_AUTH)
        add_cache(login, encrypted)
    else:
        print(FAIL_AUTH)