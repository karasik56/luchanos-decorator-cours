"""После решения задач написать функцию и задекорировать её сразу несколькими
из созданных декораторов, и посмотреть на результат и суметь объяснить его.
 Потом поменять порядок декорирования и проделать то же самое."""


def first_decorator(func):
    def wrapper(*args, **kwargs):
        print("Покупайте наших котиков")
        return func(*args, **kwargs)

    return wrapper


def second_decorator(**number_of_attempts):
    def inner(func):
        def wrapper(x, y):
            count = number_of_attempts['count']
            while count > 0:
                try:
                    return func(x, y)
                except ZeroDivisionError as error:
                    print(f'Попытка №{count} : ошибка {error}')
                    count -= 1
            return 'работа second_decorator закончена'

        return wrapper

    return inner


@first_decorator
@second_decorator(count=5)
def my_func(a, b):
    return a / b


print(my_func(5, 0))
