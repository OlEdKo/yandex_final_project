# Импортируем модуль sender_stand_request, содержащий функции для отправки HTTP-запросов 
import sender_stand_request

# Импортируем модуль data, в котором определены данные, необходимые для HTTP-запросов.
import data

def test_get_order_by_track():
    
    # Вызов функции post_new_order с телом запроса для создания нового заказа из модуля data
    response = sender_stand_request.post_new_order(data.order_body)
    assert response.status_code == 201, "Не удалось создать заказ"

    # Сохранение трэка заказа
    track_number = response.json()["track"]

    # Отправляем запрос на получение заказа по трэку
    response = sender_stand_request.get_order_by_track(track_number)

    # Проверка кода ответа
    assert response.status_code == 200