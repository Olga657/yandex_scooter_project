# Импортируем модуль sender_stand_request, содержащий функции для отправки HTTP-запросов к API.
import sender_stand_request

# Импортируем модуль data, в котором определены данные, необходимые для HTTP-запросов.
import data

# Эта функция меняет значения в параметре metroStation
def get_order_body(metroStation):
    # Копирование словаря с телом запроса из файла data, чтобы не потерять данные в исходном словаре
    current_body = data.order_body.copy()
    # Изменение значения в поле metroStation
    current_body["metroStation"] = metroStation
    # Возвращается новый словарь с нужным значением metroStation
    return current_body

def positive_assert(metroStation):
    # В переменную order_body сохраняется обновлённое тело запроса
    order_body = get_order_body(metroStation)
    # В переменную order_response сохраняется результат запроса на создание заказа:
    order_response = sender_stand_request.post_new_order(order_body)

    # Проверяется, что код ответа равен 201
    assert order_response.status_code == 201
    # Проверяется, что в ответе есть поле track и оно не пустое
    assert order_response.json()["track"] != ""

    # В переменную track сохраняется полученный трек заказа
    track = order_response.json()["track"]

    # В переменную order_by_track_response сохраняется результат запроса на получение заказа по треку заказа
    order_by_track_response = sender_stand_request.get_order_by_track(track)

    # Проверяется, что код ответа равен 200
    assert order_by_track_response.status_code == 200

# Тест на успешное создание заказа
# Параметр metroStation число
def test_create_order_get_success_response():
    positive_assert(10)
