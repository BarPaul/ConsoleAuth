from utils.files import get_cache, remove_cache
from form import register_user, authorize_user

def main():
    cache = get_cache()
    if isinstance(cache, str):
        print(f"Вы успешно авторизовались под логином {cache}")
        is_exit = input("Выйти с аккаунта? Да или нет: ").lower()
        if is_exit == "да":
            remove_cache()
        elif is_exit == "нет":
            print("Хорошо. Удачного дня!")
            return
        else:
            print("Не понял ваш ответ...")
            return main()
    page = input("Регистрация или авторизация: ").lower()
    print()
    if page == "регистрация":
        register_user()
    elif page == "авторизация":
        authorize_user()
    else:
        print("Извините, ваш запрос не понятен!")
        return main()

if __name__ == '__main__':
    main()
