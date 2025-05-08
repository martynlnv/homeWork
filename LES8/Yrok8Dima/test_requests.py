import requests
import json

base_url = 'http://5.101.50.27:8000'

def test_simple_req():
    resp = requests.get('https://httpbin.org/basic-auth/user/pass')
    assert resp.status_code == 200

#  Получить список компаний
def test_simple_req():
    resp = requests.get(base_url +'/company/list')
    assert resp.status_code == 200

# Проверим чтов заголовке объекта resp передается контент в формате JSON
def test_simple_req():
    resp = requests.get('http://5.101.50.27:8000/company/list')
    assert resp.status_code == 200
    assert resp.headers['Content-Type'] == 'application/json'

# Запишем сообщение из тела ответа в переменную responce_body в формате JSON
# и проверим что название первой компании из списка - это QA Студия 'ТестировщикЪ'
def test_simple_req():
    resp = requests.get(base_url + '/company/list')
    response_body = resp.json()
    first_company = response_body[0]
    assert first_company['name'] == "QA Студия 'ТестировщикЪ'"
    assert resp.status_code == 200
    assert  resp.headers['Content-Type'] == 'application/json'

# Авторизация
def test_auth():
    creds = {
        "username" : "harrypotter",
        "password" : "expelliarmus"
    }
    resp = requests.post(base_url + '/auth/login', json=creds)
# добавить
#   token = resp.json()['userToken']
    assert  resp.status_code == 200

# Создание компании
def test_creat_company():
    company = {
        'name': 'лошарики',
        'description': 'ясли-сад'
    }
    resp = requests.post(base_url +'/company/create', json=company)
    assert resp.status_code == 201
