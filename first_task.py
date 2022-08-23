from datetime import datetime
import requests


def log_decorator(oldfunction):
    def foo(*args, **kwargs):
        date_time = datetime.now()
        str_time = date_time.strftime('%Y-%m-%d время %H-%M-%S')
        func_name = oldfunction.__name__
        result = oldfunction(*args, **kwargs)
        with open('log/decorator_logs.txt', 'a', encoding='utf-8') as file:
            file.write(f'\nДата вызова функции: {str_time}\n'
                       f'Имя функции: {func_name}\n'
                       f'Аргументы функции: {args, kwargs}\n'
                       f'Возвращаемое значение функции: {result}\n'
                       f'{"*"*50}\n')
        return result
    return foo


@log_decorator
def get_status(*args):
    url = ','.join(args)
    response = requests.get(url=url)
    return response.status_code


@log_decorator
def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact


if __name__ == '__main__':
    get_status('https://habr.com/ru/all/')
    factorial(7)
