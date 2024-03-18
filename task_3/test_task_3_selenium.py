from configparser import ConfigParser
import pytest
from task_3_selenium import yandex_auth


config = ConfigParser()
config.read('settings.ini')
login = config['YandexAuth']['login']
password = config['YandexAuth']['password']


test_data = [
    (login, password, 'https://id.yandex.ru/'),
    ('', password, 'Логин не указан'),
    (login, '', 'Пароль не указан'),
    (login, 'some_wrong_password', 'Неверный пароль')
]

@pytest.mark.parametrize('login,password,expected', test_data)
def test_yandex_auth(login, password, expected):
    result = yandex_auth(login, password)
    assert result == expected
