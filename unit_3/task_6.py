"""6.1 Написать декоратор, который будет запрашивать у пользователя пароль при попытке функции осуществить вызов.
 Если введён верный пароль, то функция будет выполнена и вернется результат её работы.
 Если нет - в консоли появляется соответствующее сообщение.
 6.2 Параметризовать декоратор таким образом, чтобы можно было задавать индивидуальный пароль для каждой декорируемой
 функции."""


def password_decorator(valid_pass: str):
    def inner(func):
        def wrapper():
            print("Введите пароль:")
            input_password = input()
            if input_password == valid_pass:
                print("Пароль верный")
                return func()
            print("Пароль неверный, попробуйте еще раз")
            return my_func()

        return wrapper

    return inner


@password_decorator(valid_pass='666')
def my_func():
    return "Выполнение функции my_func"


print(my_func())
