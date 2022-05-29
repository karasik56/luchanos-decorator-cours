"""2.1 Написать декоратор, который внутри себя выполнял бы функцию и возвращал бы результат её работы в случае успешного выполнения.
 В случае возникновения ошибки во время выполнения функции нужно сделать так, чтобы выполнение функции было повторено ещё раз
  с теми же самыми аргументами, но не более 10 раз. Если после последней попытки функцию так и не удастся выполнить успешно,
   то бросать исключение. 2.2 Параметризовать декоратор таким образом, чтобы количество попыток выполнения функции можно было задавать
    как параметр во время декорирования."""

"""2.1 и 2.2"""


def simple_decorator(**number_of_attempts):
    def inner(func):
        def wrapper(*args, **kwargs):
            count = number_of_attempts['count']
            while count > 0:
                try:
                    return func(*args, **kwargs)
                except ZeroDivisionError as error:
                    print(f'Попытка №{count}')
                    count -= 1
            raise ZeroDivisionError("Завершение работы с исключением ZeroDivisionError")
        return wrapper
    return inner


@simple_decorator(count=10)
def my_func(a, b):
    return a / b


print(my_func(5, 0))
