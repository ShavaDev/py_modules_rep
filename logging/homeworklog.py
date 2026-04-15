import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger('typisation')
logger.setLevel(logging.DEBUG)


def setup_logging():
    if logger.handlers:
        return

    c_handler = logging.StreamHandler()
    c_handler.setLevel(logging.WARNING)

    f_handler = RotatingFileHandler(
        'logfiles/typisation.log',
        maxBytes=10000,
        backupCount=10,
        encoding='utf-8'
    )
    f_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        '%(asctime)s | [%(levelname)s] | %(name)s | %(message)s'
    )

    c_handler.setFormatter(formatter)
    f_handler.setFormatter(formatter)

    logger.addHandler(c_handler)
    logger.addHandler(f_handler)


def sum_num(x: float, y: float) -> dict:
    logger.debug('Начало суммирования!')
    sums = x + y
    result = {'sum_of_nums': sums}
    logger.info(f'Результат = {result}')


def sub_num(x: float, y: float) -> dict:
    logger.debug('Начало вычитания!')
    sub = x - y
    result = {'sub_of_nums': sub}
    logger.info(f'Результат = {result}')


def pr_num(x: float, y: float) -> dict:
    logger.debug('Начало умножения!')
    pr = x * y
    result = {'pr_of_nums': pr}
    logger.info(f'Результат = {result}')


def dev_num(x: float, y: float) -> dict:
    logger.debug('Начало деления!')
    try:
        if y == 0:
            raise ZeroDivisionError('На ноль делить нельзя!')
        else:
            dev = x / y
            result = {'dev_of_nums': dev}
            logger.info(f'Результат = {result}')
    except Exception:
        logger.exception('Деление на ноль не определено!')

    logger.debug('Продолжаем выполнение программы')


if __name__ == '__main__':
    setup_logging()
    for x, y in [(1, 2), (2, 3), (3, 4), (3, 0), (87, 4), (11, 65)]:
        sum_of_nums = sum_num(x, y)
        sub_of_nums = sub_num(x, y)
        pr_of_nums = pr_num(x, y)
        dev_of_nums = dev_num(x, y)
