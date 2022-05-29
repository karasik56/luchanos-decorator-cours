"""1.1 Написать декоратор, который перед запуском произвольной функции с произвольным набором аргументов будет
 показывать в консоли сообщение "Покупайте наших котиков!" и возвращать результат запущенной функции.
  1.2 Параметризовать декоратор таким образом, чтобы сообщение, печатаемое перед выполнением функции
   можно было задавать как параметр во время декорирования."""

"""1.1"""


def simple_decorator(func):
    def wrapper(*args, **kwargs):
        print("Покупайте наших котиков")
        res = func()
        return res
    return wrapper


@simple_decorator
def my_func(*args, **kwargs):
    return "Моя функция как-то отработала"


print(my_func())

"""1.2"""


def simple_decorator(some_string):
    def inner(func):
        def wrapper(*args, **kwargs):
            print(f'Покупайте наших котиков {some_string}')
            res = func()
            return res
        return wrapper
    return inner


@simple_decorator("или не покупайте")
def my_func(*args, **kwargs):
    return "Моя функция как-то отработала"


print(my_func())
