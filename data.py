# заголовки для HTTP-запроса, указывающие на то, что тело запроса будет в формате JSON
headers = {
    "Content-Type": "application/json"
}

# данные для создания нового заказа
order_body = {
    "firstName": "Вася",
    "lastName": "Пупкин",
    "address": "Уренгой",
    "metroStation": 4,
    "phone": "+79998887766",
    "rentTime": 5,
    "deliveryDate": "2025-11-06",
    "comment": "",
    "color": [
        ""
    ]
}