# Импорт настроек из модуля configuration, который содержит параметры конфигурации, такие как URL сервиса
import configuration

# Импорт библиотеки requests для выполнения HTTP-запросов
import requests

# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data

def get_docs():
    # Выполняем GET-запрос к URL, который складывается из базового URL-адреса сервиса
    # и пути к документации, заданных в модуле конфигурации
    # Функция возвращает объект ответа от сервера
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

# Вызываем функцию get_docs и сохраняем результат в переменную response
response = get_docs()

# Выводим в консоль HTTP-статус код полученного ответа
# Например, 200 означает успешный запрос, 404 - не найдено и т.д.
print(response.status_code)

def get_order_by_track(track):
    # Запрос на получение заказа по треку заказа
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH,
                        params={"t": track})

# Выполнение функции и сохранение ответа в переменную response
response = get_order_by_track(data.track)

# Вывод статус-кода ответа сервера в консоль
# Статус-коды HTTP сообщают о результате выполнения запроса
print(response.status_code)

def post_new_order(body):
    # Запрос на создание заказа
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)

# Выполнение функции и сохранение ответа в переменную response
response = post_new_order(data.order_body)

# Вывод статус-кода ответа сервера в консоль
# Статус-коды HTTP сообщают о результате выполнения запроса
print(response.status_code)

# Вывод номера трека заказа
print(response.json()["track"])
