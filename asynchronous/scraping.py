import asyncio
import aiohttp
from bs4 import BeautifulSoup
import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
LOGS_DIR = BASE_DIR / 'logs'
LOGS_DIR.mkdir(parents=True, exist_ok=True)

LOG_FILE = LOGS_DIR / 'scraping.log'

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - [%(levelname)s] - %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    filename=LOG_FILE,
                    filemode='w',
                    encoding='utf-8'
                    )
logger = logging.getLogger('scraper')

## 2
# async def parse_books(html: str):
#     """Логика парсинга отделена от сетевых запросов."""
#     soup = BeautifulSoup(html, 'html.parser')
#     books = soup.find_all('h3')
#     for book in books:
#         try:
#             title = book.find('a')['title']
#             logger.info(f'Название книги: {title}')
#         except Exception as e:
#             logger.exception(f'Ошибка при парсинге названия книги: {e}')
#
#
# async def fetch_url(session: aiohttp.ClientSession, url: str):
#     """Функция только качает данные, используя общую сессию."""
#     logger.debug(f'Запрос к {url}')
#     try:
#         async with session.get(url, timeout=10) as response:
#             response.raise_for_status()  # Выдаст ошибку если статус 4xx или 5xx
#             html = await response.text()
#             await parse_books(html)
#     except aiohttp.ClientError as e:
#         logger.error(f'Сетевая ошибка к {url}: {e}')
#     except Exception:
#         logger.exception('Непредвиденная ошибка!')
#
#
# async def main():
#     url = 'https://books.toscrape.com/'
#     # Создаем сессию ОДИН раз для всех будущих запросов
#     async with aiohttp.ClientSession() as session:
#         await fetch_url(session, url)
#
#
# if __name__ == '__main__':
#     asyncio.run(main())


## 1
# async def fetch_url(url):
#     logger.debug('Создание сессии')
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             logger.info('Успешное создание сессии')
#             try:
#                 logger.debug('Получение страницы')
#                 web_content = await response.text()
#                 soup = BeautifulSoup(web_content, 'html.parser')
#                 books = soup.find_all('h3')
#                 for book in books:
#                     title = book.find('a')['title']
#                     logger.info(f'Название книги: {title}')
#                 # logger.info(f'Контент страницы успешно получен{web_content}')
#             except Exception as e:
#                 logger.exception(f'Что-то пошло не так\n{e}')
#
# if __name__ == '__main__':
#     asyncio.run(fetch_url('https://books.toscrape.com/'))




## 3
import time
async def parse_books(html: str, url: str):
    """Парсинг названий книг из HTML."""
    soup = BeautifulSoup(html, 'html.parser')
    books = soup.find_all('h3')
    titles = [book.find('a')['title'] for book in books if book.find('a')]
    logger.info(f"Спарсено {len(titles)} книг с {url}")
    # Для наглядности выведем первую книгу в консоль
    if titles:
        print(f"Готово: {url} -> Первая книга: {titles[0]}")


async def fetch_url(session: aiohttp.ClientSession, url: str):
    """Асинхронная загрузка страницы."""
    logger.info(f'Начало загрузки: {url}')
    try:
        # Устанавливаем тайм-аут 10 секунд на запрос
        async with session.get(url, timeout=10) as response:
            response.raise_for_status()
            html = await response.text()  # Ждем загрузки текста
            await parse_books(html, url)
            logger.info(f'Завершено: {url}')
    except Exception as e:
        logger.error(f'Ошибка при работе с {url}: {e}')


async def main():
    urls = [
        f'https://books.toscrape.com/catalogue/page-{i}.html'
        for i in range(1, 11)  # Возьмем сразу 10 страниц для наглядности
    ]

    start_time = time.perf_counter()
    print(f"Запуск парсинга {len(urls)} страниц...")

    # Создаем одну сессию для всех запросов
    async with aiohttp.ClientSession() as session:
        # Создаем список "задач" (futures)
        tasks = []
        for url in urls:
            tasks.append(fetch_url(session, url))

        # ЗАПУСК: выполняем все задачи одновременно
        # Программа дойдет до этой точки и будет ждать, пока все скачается
        await asyncio.gather(*tasks)

    end_time = time.perf_counter()
    duration = end_time - start_time
    print(f"\nВсе готово! Затрачено времени: {duration:.2f} сек.")
    print(f"Подробности смотри в: {LOGS_DIR / 'scraping.log'}")


if __name__ == '__main__':
    # В 2026 году это стандартный запуск асинхронного приложения
    asyncio.run(main())