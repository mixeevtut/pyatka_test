import json
import requests


class SignIn:
    card = "7789004922000462"
    password = "Qqwerty123"
    url = "https://mystage.5ka.ru/api/v1/auth/signin"

    body = {
        "login": card,
        "password": password,
        "schema": "by-card"
    }

    data = json.dumps(body)
    headers = {
        'Content-Type': 'application/json;charset=UTF-8'
    }

    response = requests.post(url, data=data, headers=headers)
    print(response.text)
