"""4.1 Написать декоратор, который бы измерял время работы функции и печатал бы его на экран.
 4.2 Доработать декоратор таким образом, чтобы в логах было название запускаемой функции помимо времени исполнения.
  4.3 Доработать декоратор так, чтобы запись лога для функции велась в файл, путь к которому нужно было бы задавать
   во время декорирования, как параметр."""
import time
from datetime import datetime


def simple_decorator(path):
    def inner(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            res = func(*args, **kwargs)
            log_data = f"{func.__name__} {time.time() - start}"
            log_writer(log_data, path)
            return res
        return wrapper
    return inner


def log_writer(data, path):
    with open(f'{path}/log.txt', 'a', encoding='utf-8') as log_file:
        date_time = datetime.now()
        name_func, time_work = data.split()
        log_file.write(
            f'{date_time.strftime("%m/%d/%Y, %H:%M:%S")} Функция: {name_func}\
             Время выполнения: {round(float(time_work), 3)} сек.\n')


@simple_decorator('/home/karasik/Рабочий стол/my_projects')
def list_func(*args, **kwargs):
    my_list = [i ** 2 for i in range(10000000)]
    return my_list


@simple_decorator('/home/karasik/Рабочий стол/my_projects/logs')
def dict_func(*args, **kwargs):
    my_dict = {i: i ** 2 for i in range(10000000)}
    return my_dict


list_func()
dict_func()
