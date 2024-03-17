from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import time


def yandex_auth(login, password):
    chrome_path = ChromeDriverManager().install()
    browser_service = Service(executable_path=chrome_path)
    browser = Chrome(service=browser_service)

    browser.get('https://passport.yandex.ru/auth/')
    login_element = browser.find_element(by=By.ID, value='passp-field-login')
    login_element.click()
    login_element.send_keys(login)
    browser.find_element(by=By.ID, value='passp:sign-in').click()
    time.sleep(1)

    try:
        login_err = browser.find_element(by=By.ID, value='field:input-login:hint')
        return login_err.text.strip()
    except:
        print('Логин введен')

    passw_element = browser.find_element(by=By.ID, value='passp-field-passwd')
    passw_element.click()
    passw_element.send_keys(password)
    browser.find_element(by=By.ID, value='passp:sign-in').click()
    time.sleep(3)

    try:
        passw_err = browser.find_element(by=By.ID, value='field:input-passwd:hint')
        return passw_err.text.strip()
    except:
        print('Пароль введен')

    result = browser.current_url
    browser.close()
    return result
