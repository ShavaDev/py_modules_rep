import logging
# logging.debug("A DEBUG Message")
# logging.info("An INFO")
# logging.warning("A WARNING")
# logging.error("An ERROR")
# logging.critical("A message of CRITICAL severity")

# logging.basicConfig(level=logging.INFO,
#                     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     datefmt='%m/%d/%Y %I:%M:%S %p',
#                     filename='logfile.log',
#                     filemode='w',
#                     encoding='utf-8')
# logging.warning('Oh, Yeah!')
# logging.info('New programmer is coming!')
# logging.error('Perfect!')


# import logging
#
# # 1. Создаем логгер
# logger = logging.getLogger('BankSystem')
# logger.setLevel(logging.DEBUG)  # Общий порог (пропускать всё)
#
# # 2. Обработчик для КОНСОЛИ (только INFO и выше)
# c_handler = logging.StreamHandler()
# c_handler.setLevel(logging.INFO)
# c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
# c_handler.setFormatter(c_format)
#
# # 3. Обработчик для ФАЙЛА (только ERROR и выше)
# f_handler = logging.FileHandler('bank_errors.log', encoding='utf-8')
# f_handler.setLevel(logging.ERROR)
# f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# f_handler.setFormatter(f_format)
#
# # Добавляем обработчики к логгеру
# logger.addHandler(c_handler)
# logger.addHandler(f_handler)
#
# accounts = {"user_1": 5000, "user_2": 1000}
#
#
# def transfer_money(sender, receiver, amount):
#     # Используем logger, а не logging!
#     logger.info(f"Инициация перевода: {sender} -> {receiver} на сумму {amount}")
#
#     try:
#         if amount <= 0:
#             raise ValueError(f"Недопустимая сумма: {amount}")
#
#         if amount > 1_000_000:
#             logger.warning(f"КРУПНЫЙ ПЕРЕВОД! Сумма: {amount}")
#
#         # Логика...
#         accounts[sender] -= amount
#         accounts[receiver] += amount
#         logger.info("Транзакция завершена успешно")
#
#     except Exception:
#         # Автоматически пишет Traceback и уровень ERROR
#         logger.exception(f"Ошибка транзакции {sender} -> {receiver}")
#
#
# # Тесты
# transfer_money("user_1", "user_2", -50)  # Упадет в файл bank_errors.log
# transfer_money("user_1", "user_2", 100)  # Будет только в консоли


import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger('WarehouseBot')
logger.setLevel(logging.DEBUG)


# Выносим настройку в функцию
def setup_logging():
    # Консоль: коротко и строго по ТЗ
    c_handler = logging.StreamHandler()
    c_handler.setLevel(logging.WARNING)
    c_handler.setFormatter(logging.Formatter('[%(levelname)s] %(message)s'))

    # Файл: подробно с ротацией
    f_handler = RotatingFileHandler('logfiles/robot.log', maxBytes=2000, backupCount=3, encoding='utf-8')
    f_handler.setLevel(logging.DEBUG)
    f_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

    logger.addHandler(c_handler)
    logger.addHandler(f_handler)


def move_box(box_id, location):
    # Используем DEBUG для рутины
    logger.debug(f"Робот начал перемещение ящика {box_id}")
    try:
        if box_id < 0:
            raise ValueError(f"Некорректный ID: {box_id}")

        if location == 'Zone Red':
            logger.warning(f"Вход в опасную зону! Ящик: {box_id}")

    except Exception:
        logger.exception("Критическая ошибка при движении робота")


# Тест-драйв: забиваем лог, чтобы увидеть ротацию
if __name__ == "__main__":
    setup_logging()  # Запускаем настройку ТОЛЬКО при прямом запуске
    for i in range(50):
        move_box(i, "Zone A")

    move_box(-1, "Zone A")  # Проверим ошибку
    move_box(99, "Zone Red")  # Проверим консольный варнинг
