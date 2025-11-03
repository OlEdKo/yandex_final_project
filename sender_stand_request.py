# Импорт настроек из модуля configuration, который содержит параметры конфигурации, такие как URL сервиса
import configuration

# Импорт библиотеки requests для выполнения HTTP-запросов
import requests

# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data

# Определение функции post_new_order для отправки POST-запроса на создание нового заказа
def post_new_order(body):
    # Выполнение POST-запроса с использованием URL из конфигурационного файла, тела запроса и заголовков
    # URL_SERVICE и CREATE_ORDER_PATH объединяются для формирования полного URL для запроса
    # json=body используется для отправки данных пользователя в формате JSON
    # headers=data.headers устанавливает заголовки запроса из модуля data
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers
                         )

# Определение функции get_order_by_track для отправки GET-запроса на получение заказа по его трэку
def get_order_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_BY_TRACK_PATH,
                         params={"t": track},
                         headers=data.headers
                         )