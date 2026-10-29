import logging
import requests

1
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.StreamHandler(),                 # вывод в консоль
        logging.FileHandler("integration.log",   # и в файл
                            mode="w", encoding="utf-8")
    ]
)
logger = logging.getLogger(__name__)

#2
def run_integration_test(base_url: str = "https://jsonplaceholder.typicode.com") -> None:
    """
    Интеграционный тест:
      1) POST /posts  — создаём заказ
      2) берём id из ответа
      3) GET /posts/{id} — запрашиваем созданный заказ
    Все шаги логируются. Ошибки перехватываются и пишутся в лог.
    """
    create_url = f"{base_url}/posts"
    payload = {
        "title": "Мой тестовый заказ",
        "body": "Описание заказа",
        "userId": 1
    }

    try:
        logger.info("ШАГ 1. POST %s — создаём заказ", create_url)
        logger.info("Тело запроса: %s", payload)

        response_create = requests.post(create_url, json=payload, timeout=10)
        response_create.raise_for_status()

        logger.info("Ответ POST: status=%s, time=%.0f ms",
                    response_create.status_code,
                    response_create.elapsed.total_seconds() * 1000)

        data = response_create.json()
        post_id = data["id"]
        logger.info("Создан заказ с id=%s", post_id)

        get_url = f"{base_url}/posts/{post_id}"
        logger.info("ШАГ 2. GET %s — получаем заказ по id=%s", get_url, post_id)

        response_get = requests.get(get_url, timeout=10)
        response_get.raise_for_status()

        data_get = response_get.json()
        logger.info("Ответ GET: status=%s, id=%s, title=%s",
                    response_get.status_code,
                    data_get.get("id"),
                    data_get.get("title"))

        if str(data_get.get("id")) != str(post_id):
            logger.warning("ID в GET (%s) не совпадает с созданным (%s)!",
                           data_get.get("id"), post_id)
        else:
            logger.info("ТЕСТ ПРОЙДЕН: заказ создан и успешно прочитан по id=%s", post_id)

    except requests.exceptions.ConnectionError as e:
        logger.error("ОШИБКА СЕТИ: Не удалось связаться с сервером %s. Детали: %s",
                     base_url, e)
    except requests.exceptions.Timeout:
        logger.error("ОШИБКА СЕТИ: Сервер %s не ответил за отведённое время", base_url)
    except requests.exceptions.HTTPError as e:
        logger.error("ОШИБКА HTTP: Сервер вернул статус %s. Ответ: %s",
                     e.response.status_code if e.response else "?",
                     e.response.text[:200] if e.response else "нет тела")
    except requests.exceptions.RequestException as e:
        logger.error("ОШИБКА ЗАПРОСА: %s", e)

    except KeyError as e:
        logger.error("ОШИБКА СТРУКТУРЫ ОТВЕТА: отсутствует ключ %s в JSON", e)
    except ValueError as e:
        logger.error("ОШИБКА СТРУКТУРЫ ОТВЕТА: не удалось разобрать JSON (%s)", e)

    except Exception as e:
        logger.error("НЕОЖИДАННАЯ ОШИБКА: %s: %s", type(e).__name__, e)

if __name__ == "__main__":
    print("=" * 60)
    print("СЦЕНАРИЙ 1: УСПЕШНЫЙ ПРОГОН")
    print("=" * 60)
    run_integration_test("https://jsonplaceholder.typicode.com")

    print()
    print("=" * 60)
    print("СЦЕНАРИЙ 2: ИСКУССТВЕННЫЙ СБОЙ (неправильный URL)")
    print("=" * 60)
    run_integration_test("https://jsonplaceholder.typicode.com/postsss")