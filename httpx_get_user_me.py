import httpx

#Креды
login_payload = {
    "email": "test-user@example.com",
    "password": "test_passwd"
}

# Запрос на аутентификацию
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

#GET-запрос к /api/v1/users/me с авторизационными данными
headers = {"Authorization": "Bearer " + login_response_data['token']['accessToken']}
response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)

#Вывод на экран полученного ответа
print(response.json())
print(response.status_code)