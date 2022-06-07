"""7.1 Написать декоратор, который после выполнения функции будет возвращать результат и записывать его в текстовый файл.
 7.2 Модернизировать декоратор таким образом, чтобы можно было не только осуществлять запись в файл,
 но и в целом производить любую операцию логирования или оповещения. 7.3 Доработать декоратор таким образом,
 чтобы можно было при декорировании можно было передавать список нотификаторов."""
from datetime import datetime


def simple_decorator(*notificators):
    def inner(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            for notificator in notificators:
                if notificator == 'text_file_log':
                    text_log_writer(res)
                elif notificator == 'console_log':
                    console_log_write(res)
                else:
                    print(f'Выбран неправильный тип нотификатора {notificator}, возможно вы имели ввиду text_file_log '
                          f'или console_log')
            return res

        return wrapper

    return inner


def console_log_write(data):
    date_time = datetime.now()
    print(f'{date_time.strftime("%m/%d/%Y, %H:%M:%S")} Функция: {data}\n')


def text_log_writer(data):
    with open(f'log_task7.txt', 'a', encoding='utf-8') as log_file:
        date_time = datetime.now()
        log_file.write(
            f'{date_time.strftime("%m/%d/%Y, %H:%M:%S")} Функция: {data}\n')


@simple_decorator('text_file_log', 'console_log')
def my_func(*args, **kwargs):
    return "Отработала основная функция my_func"


my_func()
