import requests
import json

base_url = 'http://5.101.50.27:8000'
def test_get_companies():
    resp = requests.get(base_url +'/company/list')
    body = resp.json()
    assert  resp.status_code == 200
    assert len(body) > 0

def test_get_active_companies():
    # 1.Получить список всех компаний
    resp = requests.get(base_url+'/company/list')
    full_list = resp.json()

    # 2.Получить список активных компаний
    resp = requests.get(base_url+'/company/list?active=true')
    filtered_list = resp.json()

    # 3.Проверить, что список 1 > списка 2
    assert len(full_list) > len(filtered_list)

    # Получить список активных компаний
    # resp = requests.get(base_url + '/company/list', params={'active': 'true'})
    # filtered_list = resp.json()


    # 4.
def test_add_new():
    # Получить количество компаний
    resp = requests.get(base_url + '/company/list')
    body = resp.json()
    len_before = len(body)
    # Создать новую компанию
    #Получить новое количество компаний
    resp = requests.get(base_url +'/company/list')
    body = resp.json()
    len_after = len(body)
    # Проверить, что стало на 1 компанию больше
    # Проверить название и описание последней компании
    # Проверить, что id последней компании в списке равен ответу из шага 2



