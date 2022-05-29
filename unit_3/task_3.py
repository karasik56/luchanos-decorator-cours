"""3.1 Написать кэширующий декоратор. Суть в том, что если декорируемая функция будет запущена с теми
 параметрами с которыми она уже запускалась - брать результат из кэша и не производить повторное выполнение
 функции. 3.2 Сделать так, чтобы информация в кэше была актуальной не более 10 секунд. Предусмотреть механизм
 автоматической очистки кэша в процессе выполнения функций. 3.3 Параметризовать время кэширования в декораторе."""
import time


def cache_decorator(time_value):
    cache_dict = {}

    def inner(func):
        def wrapper(*args, **kwargs):
            global start
            key = str(args)
            """Проверка на наличии значение в кэше"""
            if key not in cache_dict:
                print('Добавляем значение в кэш')
                cache_dict[key] = func(*args, **kwargs)
                start = time.time()
            """Проверка на актуальность значений в кэше, в зависимости от времени"""
            if time.time() - start >= time_value:
                cache_dict.clear()
                print('Кэш очистился')
                return func(*args, **kwargs)
            return cache_dict[key]

        return wrapper

    return inner


time_value_default = 10


@cache_decorator(time_value_default)
def my_func(a, b):
    return a + b


""" создаем ситуацию с временной задержкой """
for i in range(1):
    print(my_func(2, 2))
    time.sleep(time_value_default)
    print(my_func(2, 2))
