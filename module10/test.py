import queue
import threading

import requests
from bs4 import BeautifulSoup

# Очередь для URL
url_queue = queue.Queue()

# Общий список ссылок
all_links = set()

# Блокировка для синхронизации доступа к общему списку
lock = threading.Lock()


# Функция для загрузки страницы и извлечения ссылок
def fetch_links():
    while not url_queue.empty():
        url = url_queue.get()
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                links = [a["href"] for a in soup.find_all("a", href=True)]

                # Добавляем ссылки в общий список с блокировкой
                with lock:
                    all_links.update(links)
                print(
                    f"[{threading.current_thread().name}] Обработано {url}: найдено {len(links)} ссылок"
                )
            else:
                print(
                    f"[{threading.current_thread().name}] Ошибка загрузки {url}: статус {response.status_code}"
                )
        except requests.exceptions.RequestException as e:
            print(f"[{threading.current_thread().name}] Ошибка запроса {url}: {e}")
        finally:
            url_queue.task_done()


# Основная программа
if __name__ == "__main__":
    # Список URL для парсинга
    urls = [
        "https://example.com",
        "https://www.python.org",
        "https://realpython.com",
        "https://www.wikipedia.org",
        "https://www.github.com",
        "https://www.stackoverflow.com",
    ]

    # Наполняем очередь URL
    for url in urls:
        url_queue.put(url)

    # Количество потоков
    num_threads = 5

    # Запускаем потоки
    threads = []
    for i in range(num_threads):
        t = threading.Thread(target=fetch_links, name=f"Thread-{i+1}")
        t.start()
        threads.append(t)

    # Ждем завершения всех потоков
    for t in threads:
        t.join()

    # Вывод результатов
    print("\nВсе ссылки собраны:")
    for link in all_links:
        print(link)

    print(f"\nОбщее количество уникальных ссылок: {len(all_links)}")
