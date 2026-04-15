import logging
from logging_config import setup_logging

setup_logging()
logger1 = logging.getLogger('app')
logger2 = logging.getLogger('app.operations')


def add(a, b):
    logger2.debug('Начало выполнения суммирования')
    result = a + b
    logger1.info(f'Суммирование прошло успешно, ответ {result}')


def sub(a, b):
    logger2.debug('Начало выполнения вычитания')
    result = a - b
    logger1.info(f'Вычитание прошло успешно, ответ {result}')


def mul(a, b):
    logger2.debug('Начало выполнения умножения')
    result = a * b
    logger1.info(f'Умножение прошло успешно, ответ {result}')


def div(a, b):
    logger2.debug('Начало выполнения деления')
    try:
        if b == 0:
            raise ZeroDivisionError('Деление на ноль не определено!')

        result = a / b
        logger1.info(f'Деление прошло успешно, ответ {result}')
    except Exception:
        logger1.exception('Нельзя делить на ноль!')
