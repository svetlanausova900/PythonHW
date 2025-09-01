import requests
import pytest
from requests.exceptions import RequestException

base_url = "https://ru.yougile.com/api-v2"

# авторизация
def test_auth():
    creds = {


    }
    resp = requests.post(base_url + '/auth/keys', json=creds)
    assert resp.json()["key"]
    assert resp.status_code == 201      

# создание компании/проекта (позитив)
def test_create_company_positive():

    global created_project_id
    creds = {
       
    }

    company = {
        'title': 'Ремонт',
        'users': {
            'e895f285-6701-4575-90b3-030624f7a2a6': 'admin'
        }
    }
    resp = requests.post(base_url + '/auth/keys', json=creds)
    token = resp.json()["key"]

    headers = {"Authorization": f"Bearer {token}"}

    resp = requests.post(base_url + '/projects', json=company, headers = headers)
    assert resp.status_code == 201
    response_data = resp.json()

    project_id = response_data["id"]
    print(f"Created project ID: {project_id}")

    # создание компании/проекта (негатив - нет названия Компании)
def test_create_company_negative():
    creds = {
    
    }

    company = {

        'title': '',
        'users': {
            'e895f285-6701-4575-90b3-030624f7a2a6': 'admin'
        }
    }
    resp = requests.post(base_url + '/auth/keys', json=creds)
    token = resp.json()["key"]

    headers = {"Authorization": f"Bearer {token}"}

    resp = requests.post(base_url + '/projects', json=company, headers = headers)
    assert resp.status_code == 400

#Получение списка компаний
def test_get_list():
     
    creds = {
    
    }
    resp = requests.post(base_url + '/auth/keys', json=creds)

    resp = requests.get(base_url + '/projects')

    assert "application/json" in resp.headers["Content-Type"]
    
    return resp.json()

# Изменение названия позитив
def test_change_company_positive():

    creds = {
     
    }

    resp = requests.post(base_url + '/auth/keys', json=creds)

    token = resp.json()["apikey"]

    headers = {"Authorization": f"Bearer {token}"}
    company = {
        'title': 'SkyPro',
        'users': {
            'e895f285-6701-4575-90b3-030624f7a2a6': 'admin'
        }
     }

    resp = requests.put(base_url + '/projects/396ed7e1-49fa-4573-9b20-b00d25c06050', json=company, headers = headers)

    assert resp.status_code == 200


# Изменение названия негатив(большое кол-во символов)
def test_change_company_negative():
    creds = {
    
    }

    resp = requests.post(base_url + '/auth/keys', json=creds)

    token = resp.json()["apikey"]

    headers = {"Authorization": f"Bearer {token}"}
    company = {
        'title': 'Нейминг-это основа бренда! Онлайн генератор создаст для вас слово, которое станет Вашим брендом! В современном мире в период цифровизации очень важно защитить свой бренд или не нарушить права существующего бренда. Регистрация названий (Торговой марки) — это единственный способ защитить право на свой бренд!»',
        'users': {
            'e895f285-6701-4575-90b3-030624f7a2a6': 'admin'
        }
     }

    resp = requests.put(base_url + '/projects/396ed7e1-49fa-4573-9b20-b00d25c06050', json=company, headers = headers)

    assert resp.status_code == 400